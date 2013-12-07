%define	major 3
%define libname	%mklibname openr2_ %{major}
%define develname %mklibname -d openr2

Summary:	MFC/R2 signalling over E1 lines using the DAHDI Telephony interface
Name:		openr2
Version:	1.3.3
Release:	4
License:	GPLv2
Group:		System/Servers
URL:		http://code.google.com/p/openr2/
Source0:	http://openr2.googlecode.com/files/openr2-%{version}.tar.gz
BuildRequires:	autoconf automake libtool
BuildRequires:	dahdi-devel

%description
OpenR2 is a library that implements the MFC/R2 signalling over E1 lines using
the DAHDI Telephony interface. The MF R2 tones required for the signaling are
generated by code borrowed from the LGPL library SpanDSP written by Steve
Underwood, the user has the option to provide a MF interface to use his own MF
R2 tone generation and detection so the library will use them when needed,
that's why this library does not depend directly on spandsp, libteletone or
zaptel for tone generation and detection (depends on zaptel for CAS bits and
general media transmission though)

%package -n	%{libname}
Summary:	MFC/R2 signalling over E1 lines using the DAHDI Telephony interface library
Group:          System/Libraries

%description -n	%{libname}
OpenR2 is a library that implements the MFC/R2 signalling over E1 lines using
the DAHDI Telephony interface. The MF R2 tones required for the signaling are
generated by code borrowed from the LGPL library SpanDSP written by Steve
Underwood, the user has the option to provide a MF interface to use his own MF
R2 tone generation and detection so the library will use them when needed,
that's why this library does not depend directly on spandsp, libteletone or
zaptel for tone generation and detection (depends on zaptel for CAS bits and
general media transmission though)

%package -n	%{develname}
Summary:	Development files for the openr2 library
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	openr2-devel
Provides:	openr2-devel = %{version}-%{release}

%description -n	%{develname}
OpenR2 is a library that implements the MFC/R2 signalling over E1 lines using
the DAHDI Telephony interface. The MF R2 tones required for the signaling are
generated by code borrowed from the LGPL library SpanDSP written by Steve
Underwood, the user has the option to provide a MF interface to use his own MF
R2 tone generation and detection so the library will use them when needed,
that's why this library does not depend directly on spandsp, libteletone or
zaptel for tone generation and detection (depends on zaptel for CAS bits and
general media transmission though)

This package contains development files for the openr2 library.

%prep

%setup -q

%build
autoreconf -fi
%configure2_5x --with-pic
%make

%install
%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files
%doc doc/*
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/r2proto.conf
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/r2test.conf
%attr(0755,root,root) %{_bindir}/r2dtmf_detect
%attr(0755,root,root) %{_bindir}/r2test
%{_mandir}/man5/*
%{_mandir}/man8/*

%files -n %{libname}
%doc COPYING* README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/openr2
%{_includedir}/openr2.h
%{_libdir}/*.so
