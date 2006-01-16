# TUDO
# - icons
Summary:	Provides a full screen view of all open windows
Summary(pl):	Udostêpnianie pe³noekranowego podgl±du wszystkich otwartych okien
Name:		kompose
Version:	0.5.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/kompose/%{name}-%{version}.tar.bz2
# Source0-md5:	9ae1540e91a4aeef0f71b28cf02c7869
URL:		http://kompose.berlios.de/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	imlib2-devel
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kompose currently allows a fullscreen view of all your virtual
desktops where every window is represented by a scaled screenshot of
it's own.

%description -l pl
Kompose jest programem pozwalaj±cym przegl±daæ wszystkie wirtualne
pulpity w trybie pe³noekranowym, gdzie okna reprezentowane s± jako
oddzielny obrazek.

%prep
%setup -q
# categories choice isn't probably the best
echo 'Categories=Qt;KDE;Graphics;' >> src/%{name}.desktop

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}

%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir} \
	--with-imlib2-config=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/kompose
%{_desktopdir}/kompose.desktop
%{_datadir}/apps/%{name}
#%{_iconsdir}/hicolor/*/*/kompose.png
