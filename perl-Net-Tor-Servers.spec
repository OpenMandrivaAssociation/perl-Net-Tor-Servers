%define realname   Net-Tor-Servers
%define version    0.02
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL v2 or Artistic
Group:      Development/Perl
Summary:    Perl extension to query a Tor Directory and collect information on servers
Source:     http://www.cpan.org/modules/by-module/Net/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildArch: noarch

%description
This module was written to make life a little easier for me when I have
been developing a dymanic blocklist for educational institutions to prevent
students from being able to circumvent legally required content filtering
systems.

Its nothing special, just a quick and easy way to get the data together in
an array.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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


