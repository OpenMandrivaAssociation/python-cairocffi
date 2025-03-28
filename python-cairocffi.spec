%global pypi_name cairocffi
%global pypi_oname cairocffi

Name:		python-%{pypi_name}
Version:	1.7.1
Release:	1
Group:		Development/Python
Summary:	cffi-based cairo bindings for Python
License:	MIT
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/source/c/cairocffi/cairocffi-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(cffi)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	python3dist(pip)
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
%py_build

%install
%py_install

%files
%{python_sitelib}/%{pypi_name}*
