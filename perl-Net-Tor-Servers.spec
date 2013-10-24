%define upstream_name    Net-Tor-Servers
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl extension to query a Tor Directory and collect information on servers
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/AJDIXON/Net-Tor-Servers-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module was written to make life a little easier for me when I have
been developing a dymanic blocklist for educational institutions to prevent
students from being able to circumvent legally required content filtering
systems.

Its nothing special, just a quick and easy way to get the data together in
an array.

%prep
%setup -qc

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 655145
- rebuild for updated spec-helper

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 474663
- rebuild using %%perl_convert_version

* Wed Jan 28 2009 Michael Scherer <misc@mandriva.org> 0.02-1mdv2010.1
+ Revision: 334793
- import perl-Net-Tor-Servers





