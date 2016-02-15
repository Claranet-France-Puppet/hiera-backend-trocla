%global gem_name hiera-backend-trocla

Name: rubygem-%{gem_name}
Version: 0.0.1
Release: 1%{?dist}
Summary: This is a hiera backend for the trocla password storage tool
Group: Development/Languages
License: GPLv3
URL: https://github.com/ZeroPointEnergy/hiera-backend-trocla
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?rhel} >= 7
BuildRequires: ruby(release)
%endif
BuildRequires: rubygems-devel
BuildRequires: ruby
Requires: rubygem-trocla
BuildArch: noarch

%description
This is a simple hiera backend to retrieve passwords from trocla.

The idea of this backend is to enable you to use secrets from trocla directly from your hiera data via interpolation tokens.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Jan 27 2016 mh - 0.0.1-1
- Initial package
