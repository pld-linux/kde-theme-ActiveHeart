
%define		_name ActiveHeart
%define		__name	activeheart
%define		_style_ver 1.2.1
%define		_kwin_ver 1.1

Summary:	KDE theme - %{_name}
Summary(pl.UTF-8):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	%{_style_ver}
Release:	3
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/11384-%{__name}-%{version}.tar.bz2
# Source0-md5:	80421708a5cfe26d75819bf618194e16
Source1:	http://www.kde-look.org/content/files/11460-kwin-%{__name}-%{_kwin_ver}.tar.bz2
# Source1-md5:	3e51a661dfce595469af0c39d483ff21
Patch0:		%{_name}-paths.patch
URL:		http://www.kde-look.org/content/show.php?content=11384
#See also:	http://www.kde-look.org/content/show.php?content=11460
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	unsermake
Requires:	kde-style-%{_name}
Requires:	kde-colorscheme-%{_name}
Requires:	kde-decoration-%{_name}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The concept of ActiveHeart theme is a harmony of sharpness and
softness. And this style was created based on keramik.

%description -l pl.UTF-8
Ideą motywu ActiveHeart jest harmonia między ostrością a łagodnością.
Ten styl został stworzony w oparciu o keramik.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl.UTF-8):	Styl do KDE - %{_name}
Group:		Themes

%description -n kde-style-%{_name}
A higly customizable convex style which feature a unique, soft look
while preserving sharpness.

%description -n kde-style-%{_name} -l pl.UTF-8
Dostosowywalny, wypukły styl tworzący miękki i lekki wygląd z
zachowaniem ostrości obrazu.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
A tranquil colorscheme with sand-colored window background and violet
selections.

%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Stonowany schemat kolorów z tłem okien w kolorze piasku i fioletowymi
zaznaczeniami.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl.UTF-8):	Dekoracja kwin - %{_name}
Group:		Themes
Epoch:		1
Version:	%{_kwin_ver}
URL:		http://www.kde-look.org/content/show.php?content=11460
Requires:	kdebase-desktop-libs >= 9:3.2.0

%description -n kde-decoration-%{_name}
A kwin decoration with shadows under buttons and solid window borders.
The buttons and the window title are placed in a rectangular (with
rounded corners), convex area which has a shiny look.

%description -n kde-decoration-%{_name} -l pl.UTF-8
Dekoracja kwin z cieniami pod przyciskami oraz solidnymi brzegami
okien. Przyciski i tytuł okna są umieszczone na prostokątnym, wypukłym
obszrze z zaokrąglonymi brzegami. Obszar ten sprawia wrażenie
lśniącego.

%prep
%setup -q -c -a1
%patch0 -p0
%build
cd %{__name}-%{_style_ver}
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

cd ../kwin-%{__name}-%{_kwin_ver}
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.cvs
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C %{__name}-%{_style_ver} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C kwin-%{__name}-%{_kwin_ver} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files

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
