
%define         _name ActiveHeart
%define		__name	activeheart
%define		_style_ver 1.2.1
%define		_kwin_ver 1.1

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	%{_style_ver}
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/11384-%{__name}-%{version}.tar.bz2
# Source0-md5:	80421708a5cfe26d75819bf618194e16
Source1:	http://www.kde-look.org/content/files/11460-kwin-%{__name}-%{_kwin_ver}.tar.bz2
# Source1-md5:	3e51a661dfce595469af0c39d483ff21
URL:		http://www.kde-look.org/content/show.php?content=11384
#See also:	http://www.kde-look.org/content/show.php?content=11460
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	unsermake
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The concept of ActiveHeart theme is a harmony of sharpness and
softness. And this style was created based on keramik.

%description -l pl
Ide± motywu ActiveHeart jest harmonia miêdzy ostro¶ci± a ³agodno¶ci±.
Ten styl zosta³ stworzony w oparciu o keramik.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes

%description -n kde-style-%{_name}
A higly customizable convex style which feature a unique, soft look
while preserving sharpness.

%description -n kde-style-%{_name} -l pl
Dostosowywalny, wypuk³y styl tworz±cy miêkki i lekki wygl±d z
zachowaniem ostro¶ci obrazu.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
A tranquil colorscheme with sand-colored window background and violet
selections.

%description -n kde-colorscheme-%{_name} -l pl
Stonowany schemat kolorów z t³em okien w kolorze piasku i fioletowymi
zaznaczeniami.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl):	Dekoracja kwin - %{_name}
Group:		Themes
Epoch:		1
Version:	%{_kwin_ver}
Url:		http://www.kde-look.org/content/show.php?content=11460
Requires:	kdebase-desktop-libs >= 9:3.2.0

%description -n kde-decoration-%{_name}
A kwin decoration with shadows under buttons and solid window borders.
The buttons and the window title are placed in a rectangular (with
rounded corners), convex area which has a shiny look.

%description -n kde-decoration-%{_name} -l pl
Dekoracja kwin z cieniami pod przyciskami oraz solidnymi brzegami
okien. Przyciski i tytu³ okna s± umieszczone na prostok±tnym, wypuk³ym
obszrze z zaokr±glonymi brzegami. Obszar ten sprawia wra¿enie
l¶ni±cego.

%prep
# setup with -a1 broke unsermake and i understand we shouldnt build
# outside the builddir, so here goes:

cd $RPM_BUILD_DIR
if [ -d %{name}-%{version} ]; then
rm -rf %{name}-%{version}
fi
mkdir %{name}-%{version}
cd %{name}-%{version}
%{__tar} xfj %{SOURCE0} -C ./
%{__tar} xfj %{SOURCE1} -C ./

%build
cd $RPM_BUILD_DIR/%{name}-%{version}/%{__name}-%{_style_ver}
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs
%configure
%{__make}

cd $RPM_BUILD_DIR/%{name}-%{version}/kwin-%{__name}-%{_kwin_ver}
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

cd $RPM_BUILD_DIR/%{name}-%{version}/%{__name}-%{_style_ver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_DIR/%{name}-%{version}/kwin-%{__name}-%{_kwin_ver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop
