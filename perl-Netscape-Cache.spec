%include	/usr/lib/rpm/macros.perl
%define	pdir	Netscape
%define	pnam	Cache
Summary:	Netscape-Cache perl module
Summary(pl):	Modu� perla Netscape-Cache
Name:		perl-Netscape-Cache
Version:	0.44
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netscape-Cache - module for accessing Netscape cache files.

%description -l pl
Netscape-Cache umo�liwia dost�p do cache'a Nestscape'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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
