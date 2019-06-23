%global pypi_name cairocffi
%global pypi_oname cairocffi

Name:           python-%{pypi_name}
Version:	1.0.2
Release:        1
Group:          Development/Python
Summary:        cffi-based cairo bindings for Python

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/0f/0f/7e21b5ddd31b610e46a879c0d21e222dd0fef428c1fc86bbd2bd57fed8a7/cairocffi-1.0.2.tar.gz
#Patch0:         cairocffi-0.5.1-fix-python3-build.patch

BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
BuildRequires:  python-cffi

%rename python3-%{pypi_name}

%description
cffi-based cairo bindings for Python

%prep
%setup -q -n %{pypi_oname}-%{version}
%apply_patches

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
