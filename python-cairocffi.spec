%global pypi_name cairocffi
%global pypi_oname cairocffi

Name:		python-%{pypi_name}
Version:	1.2.0
Release:	1
Group:		Development/Python
Summary:	cffi-based cairo bindings for Python
License:	MIT
URL:		http://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/84/ca/0bffed5116d21251469df200448667e90acaa5131edea869b44a3fbc73d0/cairocffi-1.2.0.tar.gz
#Patch0:         cairocffi-0.5.1-fix-python3-build.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(cffi)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(cairo)
Requires:	%{_lib}cairo2
Requires:	python3dist(cffi)
%rename python3-%{pypi_name}

%description
cffi-based cairo bindings for Python.

%prep
%autosetup -n %{pypi_oname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
