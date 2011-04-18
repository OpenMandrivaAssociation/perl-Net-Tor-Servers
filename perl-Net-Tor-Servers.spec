%define upstream_name    Net-Tor-Servers
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl extension to query a Tor Directory and collect information on servers
License:    GPLv2+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module was written to make life a little easier for me when I have
been developing a dymanic blocklist for educational institutions to prevent
students from being able to circumvent legally required content filtering
systems.

Its nothing special, just a quick and easy way to get the data together in
an array.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
