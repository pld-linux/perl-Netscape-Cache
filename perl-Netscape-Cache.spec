%include	/usr/lib/rpm/macros.perl
Summary:	Netscape-Cache perl module
Summary(pl):	Modu³ perla Netscape-Cache
Name:		perl-Netscape-Cache
Version:	0.44
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Netscape/Netscape-Cache-%{version}.tar.gz
Patch0:		perl-Netscape-Cache-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f examples/*~
install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Netscape/Cache
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Netscape/Cache.pm
%{perl_sitearch}/auto/Netscape/Cache

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}
