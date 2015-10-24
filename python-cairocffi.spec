%global pypi_name cairocffi
%global pypi_oname cairocffi

%define python2 1

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        2
Group:          Development/Python
Summary:        cffi-based cairo bindings for Python

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/c/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz
Patch0:         cairocffi-0.5.1-fix-python3-build.patch

BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools

%rename python3-%{pypi_name}

%description
cffi-based cairo bindings for Python

%if %python2
%package -n python2-%{pypi_name}
Summary:        cffi-based cairo bindings for Python
Group:          Development/Python

BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools

%description -n python2-%{pypi_name}
cffi-based cairo bindings for Python
%endif

%prep
%setup -q -n %{pypi_oname}-%{version}
%apply_patches

%if %python2
cp -a . %{py2dir}
%endif

%build
%{__python} setup.py build

%if %python2
pushd %{py2dir}
LANG="en_US.UTF-8" %{__python2} setup.py build
popd
%endif

%install
%if %python2
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*

%if %python2
%files -n python2-%{pypi_name}
%{python2_sitelib}/%{pypi_name}*
%endif

