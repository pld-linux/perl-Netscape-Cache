#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Netscape
%define	pnam	Cache
Summary:	Netscape::Cache Perl module
Summary(cs):	Modul Netscape::Cache pro Perl
Summary(da):	Perlmodul Netscape::Cache
Summary(de):	Netscape::Cache Perl Modul
Summary(es):	Módulo de Perl Netscape::Cache
Summary(fr):	Module Perl Netscape::Cache
Summary(it):	Modulo di Perl Netscape::Cache
Summary(ja):	Netscape::Cache Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Netscape::Cache ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Netscape::Cache
Summary(pl):	Modu³ Perla Netscape::Cache
Summary(pt):	Módulo de Perl Netscape::Cache
Summary(pt_BR):	Módulo Perl Netscape::Cache
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Netscape::Cache
Summary(sv):	Netscape::Cache Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Netscape::Cache
Summary(zh_CN):	Netscape::Cache Perl Ä£¿é
Name:		perl-Netscape-Cache
Version:	0.45
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
%if %{!?_with_tests:0}%{?_with_tests:1}
BuildRequires:	db1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netscape::Cache - module for accessing Netscape cache files.

%description -l pl
Netscape::Cache umo¿liwia dostêp do cache'a Nestscape'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL
%{__make}
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f examples/*~
rm -f examples/*.orig
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Netscape/Cache.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/nscache
%{_examplesdir}/%{name}-%{version}/[Rbc]*
