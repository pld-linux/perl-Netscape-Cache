%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Netscape-Cache perl module
Summary(pl):	Modu� perla Netscape-Cache
Name:		perl-Netscape-Cache
Version:	0.42
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Netscape/Netscape-Cache-%{version}.tar.gz
Patch:		perl-Netscape-Cache-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Netscape-Cache - module for accessing Netscape cache files.

%description -l pl
Netscape-Cache umo�liwia dost�p do cache'a Nestscape'a.

%prep
%setup -q -n Netscape-Cache-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

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

/usr/src/examples/%{name}-%{version}
