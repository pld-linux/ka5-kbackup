%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kbackup
Summary:	Kbackup
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	767bf9430ff7b348ebea04426cc9aae2
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-karchive-devel >= 5.46.0
BuildRequires:	kf5-kdoctools-devel >= 5.46.0
BuildRequires:	kf5-ki18n-devel >= 5.46.0
BuildRequires:	kf5-kiconthemes-devel >= 5.46.0
BuildRequires:	kf5-kio-devel >= 5.46.0
BuildRequires:	kf5-knotifications-devel >= 5.46.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.46.0
BuildRequires:	kf5-kxmlgui-devel >= 5.46.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBackup is an application that lets you back up any folders or files
in a tar archive to a local folder, e.g. a locally mounted device like
a ZIP drive, USB stick, etc. or a remote URL.

Features

- Using profile files with definitions for Folders and files to be
  included or excluded from the backup
- The backup target can be either a locally mounted device like a ZIP
  drive, USB stick, etc. or any remote URL
- Running automated backups without using a graphical user interface

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackup
%{_desktopdir}/org.kde.kbackup.desktop
%{_iconsdir}/hicolor/16x16/apps/kbackup.png
%{_iconsdir}/hicolor/16x16/mimetypes/text-x-kbp.png
%{_iconsdir}/hicolor/22x22/actions/kbackup_cancel.png
%{_iconsdir}/hicolor/22x22/actions/kbackup_runs.png
%{_iconsdir}/hicolor/22x22/actions/kbackup_start.png
%{_iconsdir}/hicolor/32x32/apps/kbackup.png
%{_iconsdir}/hicolor/32x32/mimetypes/text-x-kbp.png
%dir %{_datadir}/kxmlgui5/kbackup
%{_datadir}/kxmlgui5/kbackup/kbackupui.rc
%{_datadir}/metainfo/org.kde.kbackup.appdata.xml
%{_datadir}/mime/packages/kbackup.xml
