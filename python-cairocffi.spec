%global pypi_name cairocffi
%global pypi_oname cairocffi

%define python3 0

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1
Group:          Development/Python
Summary:        cffi-based cairo bindings for Python

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/c/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz
Patch0:         cairocffi-0.5.1-fix-python3-build.patch

BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools

%description
cffi-based cairo bindings for Python

%if %python3
%package -n python3-%{pypi_name}
Summary:        cffi-based cairo bindings for Python
Group:          Development/Python

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
cffi-based cairo bindings for Python
%endif

%prep
%setup -q -n %{pypi_oname}-%{version}
%apply_patches

%if %python3
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if %python3
pushd %{py3dir}
LANG="en_US.UTF-8" %{__python3} setup.py build
popd
%endif

%install
%if %python3
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*

%if %python3
%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}*
%endif

