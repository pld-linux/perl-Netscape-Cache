%include	/usr/lib/rpm/macros.perl
Summary:	Netscape-Cache perl module
Summary(pl):	Modu³ perla Netscape-Cache
Name:		perl-Netscape-Cache
Version:	0.44
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Netscape/Netscape-Cache-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netscape-Cache - module for accessing Netscape cache files.

%description -l pl
Netscape-Cache umo¿liwia dostêp do cache'a Nestscape'a.

%prep
%setup -q -n Netscape-Cache-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f examples/*~
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Netscape/Cache.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
