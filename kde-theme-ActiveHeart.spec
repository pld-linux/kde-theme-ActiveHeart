
%define         _name ActiveHeart
%define		__name	activeheart
%define		_style_ver 1.1.7
%define		_kwin_ver 1.0.2

Summary:        KDE theme - %{_name}
Summary(pl):    Motyw KDE - %{_name}
Name:           kde-theme-%{_name}
Version:        %{_style_ver}
Release:        2
License:        GPL
Group:          Themes
Source0:	http://www.kde-look.org/content/files/11384-%{__name}-%{version}.tar.bz2
# Source0-md5:	c08a703fad663c600290416030c4baea
Source1:	http://www.kde-look.org/content/files/11460-kwin-%{__name}-1.0.2.tar.bz2
# Source1-md5:	5304ed670c7212961631ace667167c43
Patch0:		%{name}-global_cs.patch
URL:		http://www.kde-look.org/content/show.php?content=11384
#See also:	http://www.kde-look.org/content/show.php?content=11460
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRequires:	unsermake
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is

%description -l pl
%{_name} a theme

%package -n kde-style-%{_name}
Summary:        KDE style - %{_name}
Summary(pl):    Styl do KDE - %{_name}
Group:          Themes
Requires:       kdelibs

%description -n kde-style-%{_name}
%{_name} is a slicker style that was designed to look nice with
slicker. To developer's surprise, this style looks good even without
slicker.

%description -n kde-style-%{_name} -l pl
%{_name} to styl stworzony by wspó³gra³ z aplikacj± slicker. Ku
zaskoczeniu twórców, styl ten jednak okaza³ siê piêknie wygl±daæ nawet
bez slickera.

%package -n kde-icons-%{_name}
Summary:        KDE style - %{_name}
Summary(pl):    Styl do KDE - %{_name}
Group:          Themes
Requires:       kdelibs

%description -n kde-icons-%{_name}
%{_name} is a slicker icons theme that was designed to look nice with
slicker style.

%description -n kde-icons-%{_name} -l pl
%{_name} to motyw ikon stworzony by wspó³gra³ ze stylem slicker.

%package -n kde-colorscheme-%{_name}
Summary:        Color scheme for KDE style - %{_name}
Summary(pl):    Schemat kolorów do stylu KDE - %{_name}
Group:          Themes
Requires:       kdebase-core

%description -n kde-colorscheme-%{_name}
Color scheme for KDE style - %{_name}

%description -n kde-colorscheme-%{_name} -l pl
Schemat kolorów do stylu KDE - %{_name}


%package -n kde-wallpaper-%{_name}
Summary:        KDE wallpaper - %{_name}
Summary(pl):    Tapeta do KDE - %{_name}
Group:          Themes
# Contains /usr/share/wallpapers
Requires:       kdelibs

%description -n kde-wallpaper-%{_name}
A wallpaper to go with KDE slicker style.

%description -n kde-wallpaper-%{_name} -l pl
Tapeta pasuj±ca do stylu KDE slicker.

%package -n kde-splashplugin-%{_name}
Summary:        ksplash plugin %{_name}
Summary(pl):    Wtyczka ksplash %{_name}
Group:          X11/Amusements
Requires:       kdebase-desktop

%description -n kde-splashplugin-%{_name}
ksplash plugin %{_name}

%description -n kde-splashplugin-%{_name} -l pl
Wtyczka ksplash %{_name}


%package -n kde-colorscheme-%{_name}-thinkeramik
Summary:        Color scheme for %{_name} theme to go with thinkeramik style
Summary(pl):    Schemat kolorów dla motywu %{_name} pasuj±cy do stylu thinkeramik
Group:          Themes
Requires:       kdebase-core
Requires:       kde-style-thinkeramik

%description -n kde-colorscheme-%{_name}-thinkeramik
Color scheme for %{_name} theme to go with thinkeramik style.

%description -n kde-colorscheme-%{_name}-thinkeramik -l pl
Schemat kolorów dla motywu %{_name} pasuj±cy do stylu thinkeramik.

%package -n kde-decoration-%{_name}
Summary:        Kwin decoration - %{_name}
Summary(pl):    Dekoracja kwin - %{_name}
Group:          Themes
Version:        %{_kwin_ver}
Requires:       kdebase-desktop-libs

%description -n kde-decoration-%{_name}
Kwin decoration - %{_name}.

%description -n kde-decoration-%{_name} -l pl
Dekoracja kwin - %{_name}.

%package -n kde-splash-%{_name}
Summary:        Splash screen %{_name} theme
Summary(pl):    Obrazek startowy dla motywu %{_name}
Group:          Themes
Requires:       kdebase-desktop >= 9:3.1.90

%description -n kde-splash-%{_name}
Splash screen %{_name} theme.

%description -n kde-splash-%{_name} -l pl
Obrazek startowy dla motywu %{_name}.

%package -n kde-kside-%{_name}
Summary:        Kicker sidebar from %{_name}
Summary(pl):    Boczny pasek do menu kde z motywu %{_name}
Group:          Themes
Obsoletes:      kde-kside
Provides:       kde-kside
Requires:       kdebase-kicker >= 9:3.1.90.030726-2

%description -n kde-kside-%{_name}
Kicker sidebar from %{_name}.

%description -n kde-kside-%{_name} -l pl
Boczny pasek do menu kde z motywu %{_name}.

%package -n kopete-emoticons-%{_name}
Summary:        Kopete emoticons from %{_name} theme
Summary(pl):    Emotikony do kopete z tematu %{_name}
Group:          Themes
Requires:       kdenetwork-kopete

%description -n kopete-emoticons-%{_name}
Kopete emoticons from %{_name} theme.

%description -n kopete-emoticons-%{_name} -l pl
Emotikony do kopete z tematu %{_name}.

%package -n xmms-skin-%{_name}
Summary:        An xmms skin %{_name} theme
Summary(pl):    Skórka dla XMMS-a z motywu %{_name}
Group:          Themes
Requires:       xmms

%description -n xmms-skin-%{_name}
An xmms skin %{_name} theme.

%description -n xmms-skin-%{_name} -l pl
Skórka dla XMMS-a z motywu %{_name}.

%package -n kde-decoration-icewm-%{_name}
Summary:        Icewm window decoration for kwin - %{_name}
Summary(pl):    Dekoracja icewm dla kwin - %{_name}
Group:          Themes
Requires:       kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
Icewm window decoration for kwin - %{_name}.

%description -n kde-decoration-icewm-%{_name} -l pl
Dekoracja icewm dla kwin - %{_name}.


%prep
%setup -q -n %{__name}-%{_style_ver} -b1
%patch0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
cp /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure
%{__make}

cd ../kwin-%{__name}-%{_kwin_ver}
cp /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create dirs if necessary
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd ../kwin-%{__name}-%{_kwin_ver}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc

##%files -n kde-icons-%{_name}
##%defattr(644,root,root,755)
##%{_iconsdir}/*

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

##%files -n kde-wallpaper-%{_name}
##%defattr(644,root,root,755)
##%{_datadir}/wallpapers/*

##%files -n kde-splashplugin-%{_name}
##%defattr(644,root,root,755)
##%{_datadir}/apps/ksplash/Themes/

##%files -n kde-colorscheme-%{_name}-thinkeramik
##%defattr(644,root,root,755)
##%{_datadir}/apps/kdisplay/color-schemes/*.kcmrc

##%files -n kde-splash-%{_name}
##%defattr(644,root,root,755)
##%{_datadir}/apps/ksplash/Themes/

##%files -n kde-kside-%{_name}
##%defattr(644,root,root,755)
##%{_datadir}/apps/kicker/pics/*

##%files -n kopete-emoticons-%{_name}
##%defattr(644,root,root,755)
##%{_datadir}/apps/kopete/pics/emoticons/*

##%files -n xmms-skin-%{_name}
##%defattr(644,root,root,755)
##%{xmms_datadir}/Skins/*

##%files -n kde-decoration-icewm-%{_name}
##%defattr(644,root,root,755)
##%{_datadir}/apps/kwin/icewm-themes/*
