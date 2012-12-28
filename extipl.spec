Summary:	Yet Another Boot Selector for IBM-PC compatibles
Name:		extipl
Version:	5.04
Release:	18
URL:		http://extipl.sourceforge.jp/htdoc-en/extipl.html
Source0:	http://www.tsden.org/takamiti/extipl/archs/%{name}-%{version}.tar.bz2
License:	GPL+
Group:		System/Kernel and hardware
BuildRequires:	nasm
Exclusivearch:	%{ix86} x86_64
Patch1:		extipl-5.03-fix-manpage.patch
# Fix a nasm syntax error - 'crc32' is now a keyword in nasm
# - AdamW 2007/10
Patch2:		extipl-5.04-syntax.patch
# From Debian - fixes build problems - AdamW 2007/10
Patch3:		extipl-5.04-debian.patch
# From Debian bug - fix build on x86_64
Patch4:		extipl-5.04-debian2.patch

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
%patch2 -p1 -b .syntax~
%patch3 -p1 -b .debian~
%patch4 -p1 -b .debian2~

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
install src/%{name} -D %{buildroot}%{_sbindir}/%{name}

install -d %{buildroot}%{_prefix}/lib/%{name}
install -m644 src/{pollux,castor,altair,aldebaran}.bin %{buildroot}%{_prefix}/lib/%{name}

install -m644 src/extipl.8.in -D %{buildroot}%{_mandir}/man8/extipl.8

%files
%doc uninstall_linux_or_grub.txt doc/English/*
%{_sbindir}/*
%{_prefix}/lib/%{name}
%{_mandir}/*/*

%changelog
* Fri Dec 28 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.04-18
- cleanups
- update url

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 5.04-17mdv2011.0
+ Revision: 664165
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 5.04-16mdv2011.0
+ Revision: 605114
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 5.04-15mdv2010.1
+ Revision: 522579
- rebuilt for 2010.1

* Fri Oct 09 2009 Olivier Blin <oblin@mandriva.com> 5.04-14mdv2010.0
+ Revision: 456407
- move files from /usr/lib64/extipl to /usr/lib/extipl,
  since they really are no x86_64 files
  (mimic commit 60126 from pixel on syslinux)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 5.04-13mdv2010.0
+ Revision: 424394
- rebuild

* Mon Mar 30 2009 Pascal Terjan <pterjan@mandriva.org> 5.04-12mdv2009.1
+ Revision: 362286
- Enable build on x86_64 and add patch from debian bugtracker

* Mon Mar 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.04-11mdv2009.1
+ Revision: 347460
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 5.04-10mdv2009.0
+ Revision: 220738
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 05 2007 Adam Williamson <awilliamson@mandriva.org> 5.04-9mdv2008.1
+ Revision: 106206
- rebuild for lzma permission issue (#35309)

* Sun Nov 04 2007 Adam Williamson <awilliamson@mandriva.org> 5.04-8mdv2008.1
+ Revision: 105672
- add extipl-5.04-debian.patch (from debian) to fix C build errors
- add extipl-5.04-syntax.patch to fix nasm syntax errors
- rebuild for 2008
- new license policy


* Fri Jan 12 2007 Pixel <pixel@mandriva.com> 5.04-7mdv2007.0
+ Revision: 108022
- use mkrel
- Import extipl

* Wed Oct 12 2005 Pixel <pixel@mandriva.com> 5.04-6mdk
- rebuild

* Sat Aug 14 2004 Pixel <pixel@mandrakesoft.com> 5.04-5mdk
- rebuild

