Summary:	Provides a full screen view of all open windows
Summary(pl):	Udostêpnia pe³noekranowy podgl±d wszystkich otwartych okien
Name:		kompose
Version:	0.4.2
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/kompose/%{name}-%{version}.tar.bz2
# Source0-md5:	b51839098432590c0903da3e75a853ac
URL:		http://kompose.berlios.de
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kompose currently allows a fullscreen view of all your virtual
desktops where every window is represented by a scaled screenshot of
it's own.

%description -l pl
Kompose jest programem pozwalaj±cym przegl±daæ wszystkie wirtualne
pulpity w trybie pe³no ekranowym, gdzie okna reprezêntowane s± jako
oddzielny obrazek.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/kompose
%{_desktopdir}/kompose.desktop
%{_datadir}/apps/%{name}/*
%{_kdedocdir}/en/%{name}/*
%{_iconsdir}/hicolor/16x16/apps/kompose.png
%{_iconsdir}/hicolor/32x32/apps/kompose.png
