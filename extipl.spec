Summary:	Yet Another Boot Selector for IBM-PC compatibles
Name:		extipl
Version:	5.04
Release:	29
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		https://extipl.sourceforge.jp/htdoc-en/extipl.html
Source0:	http://www.tsden.org/takamiti/extipl/archs/%{name}-%{version}.tar.bz2
Patch1:		extipl-5.03-fix-manpage.patch
# Fix a nasm syntax error - 'crc32' is now a keyword in nasm
# - AdamW 2007/10
Patch2:		extipl-5.04-syntax.patch
# From Debian - fixes build problems - AdamW 2007/10
Patch3:		extipl-5.04-debian.patch
# From Debian bug - fix build on x86_64
Patch4:		extipl-5.04-debian2.patch
ExclusiveArch:	%{ix86} x86_64
BuildRequires:	nasm

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
%autopatch -p1

cat > uninstall_linux_or_grub.txt <<EOF
If you want to remove Linux, you must be careful to replace LILO or GRUB with
something else.

The equivalent of the Microsoft DOS/Windows(R) "fdisk /mbr" is:
% dd if=/usr/lib/extipl/aldebaran.bin of=/dev/hda
where you must replace hda with your first hard drive (eg: sda, hdc...)
EOF

%build
%setup_compile_flags
%make -C src

%install
install src/%{name} -D %{buildroot}%{_sbindir}/%{name}

install -d %{buildroot}%{_prefix}/lib/%{name}
install -m644 src/{pollux,castor,altair,aldebaran}.bin %{buildroot}%{_prefix}/lib/%{name}

install -m644 src/extipl.8.in -D %{buildroot}%{_mandir}/man8/extipl.8

%files
%doc uninstall_linux_or_grub.txt doc/English/*
%{_sbindir}/*
%{_prefix}/lib/%{name}
%{_mandir}/*/*

