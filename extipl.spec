%define	name	extipl
%define	version	5.04
%define release	%mkrel 8

Summary:	Yet Another Boot Selector for IBM-PC compatibles
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.tsden.org/ryutaroh/extipl/extipl.html
Source0:	http://www.tsden.org/takamiti/extipl/archs/%{name}-%{version}.tar.bz2
License:	GPL+
Group:		System/Kernel and hardware
BuildRequires:	nasm
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Exclusivearch:	%{ix86}
Patch1:		%{name}-5.03-fix-manpage.patch

%description
Extended-IPL is a boot selector which is upper compatible with 
original IBM IPL. This package includes the installer for this
boot code which is written into MBR of your hard disk.

With this boot selector, you can select a partition from 
all the partitions including the logical partitions as well as 
the primary ones in all the BIOS supported disks when booting a PC,
and then it will boot up the OS reside at the selected partition.

%prep
%setup -q
%patch1 -p1

cat > uninstall_linux_or_grub.txt <<EOF
If you want to remove Linux, you must be careful to replace LILO or GRUB with
something else.

The equivalent of the Microsoft DOS/Windows(R) "fdisk /mbr" is:
% dd if=/usr/lib/extipl/aldebaran.bin of=/dev/hda
where you must replace hda with your first hard drive (eg: sda, hdc...)
EOF

%build
%make -C src

%install
rm -rf $RPM_BUILD_ROOT

install src/%{name} -D $RPM_BUILD_ROOT%{_sbindir}/%{name}

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m 644 src/{pollux,castor,altair,aldebaran}.bin $RPM_BUILD_ROOT%{_libdir}/%{name}

install -D -m 644 src/extipl.8.in $RPM_BUILD_ROOT%{_mandir}/man8/extipl.8


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc uninstall_linux_or_grub.txt doc/English/*
%{_sbindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*

