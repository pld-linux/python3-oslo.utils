#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (looong, timeouts happen)

Summary:	Oslo Utility library
Summary(pl.UTF-8):	Biblioteka narzędziowa Oslo
Name:		python3-oslo.utils
Version:	9.1.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/oslo-utils/
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.utils/oslo_utils-%{version}.tar.gz
# Source0-md5:	9816a59114cde328d5909b47bd4289c0
URL:		https://pypi.org/project/oslo.utils/
BuildRequires:	python3-pbr >= 6.1.1
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML >= 3.13
BuildRequires:	python3-debtcollector >= 1.2.0
BuildRequires:	python3-ddt >= 1.0.1
BuildRequires:	python3-eventlet >= 0.18.4
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-iso8601 >= 0.1.11
BuildRequires:	python3-netaddr >= 0.10.0
BuildRequires:	python3-oslo.config >= 5.2.0
BuildRequires:	python3-oslo.i18n >= 3.15.3
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-packaging >= 20.4
BuildRequires:	python3-psutil >= 3.2.2
BuildRequires:	python3-pyparsing >= 2.1.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 2.2.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with doc}
BuildRequires:	python3-openstackdocstheme >= 2.2.0
BuildRequires:	python3-reno >= 3.1.0
BuildRequires:	sphinx-pdg-3 >= 2.0.0
%endif
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The oslo.utils library provides support for common utility type
functions, such as encoding, exception handling, string manipulation,
and time handling.

%description -l pl.UTF-8
Biblioteka oslo.utils udostępnia wspólne funkcje narzędziowe, takie
jak kodowanie, obsługa wyjątków, operacje na łańcuchach znaków czy
obsługa czasu.

%package apidocs
Summary:	API documentation for Python oslo.utils module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslo.utils
Group:		Documentation

%description apidocs
API documentation for Pythona oslo.utils module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslo.utils.

%prep
%setup -q -n oslo_utils-%{version}

%build
%py3_build

%if %{with tests}
stestr-3 run
%endif

%if %{with doc}
sphinx-build-3 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/oslo_utils/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/oslo_utils
%{py3_sitescriptdir}/oslo.utils-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,reference,user,*.html,*.js}
%endif
