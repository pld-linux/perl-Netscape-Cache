#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	Netscape
%define		pnam	Cache
Summary:	Netscape::Cache Perl module
Summary(cs.UTF-8):	Modul Netscape::Cache pro Perl
Summary(da.UTF-8):	Perlmodul Netscape::Cache
Summary(de.UTF-8):	Netscape::Cache Perl Modul
Summary(es.UTF-8):	Módulo de Perl Netscape::Cache
Summary(fr.UTF-8):	Module Perl Netscape::Cache
Summary(it.UTF-8):	Modulo di Perl Netscape::Cache
Summary(ja.UTF-8):	Netscape::Cache Perl モジュール
Summary(ko.UTF-8):	Netscape::Cache 펄 모줄
Summary(nb.UTF-8):	Perlmodul Netscape::Cache
Summary(pl.UTF-8):	Moduł Perla Netscape::Cache
Summary(pt.UTF-8):	Módulo de Perl Netscape::Cache
Summary(pt_BR.UTF-8):	Módulo Perl Netscape::Cache
Summary(ru.UTF-8):	Модуль для Perl Netscape::Cache
Summary(sv.UTF-8):	Netscape::Cache Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Netscape::Cache
Summary(zh_CN.UTF-8):	Netscape::Cache Perl 模块
Name:		perl-Netscape-Cache
Version:	0.46
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f39bc40fc2c3f61219ac5a3d4a39ccc2
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Netscape-Cache/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	db1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netscape::Cache - module for accessing Netscape cache files.

%description -l pl.UTF-8
Netscape::Cache umożliwia dostęp do cache'a Nestscape'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f examples/*~
rm -f examples/*.orig
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Netscape/Cache.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/nscache
%{_examplesdir}/%{name}-%{version}/[Rbc]*
