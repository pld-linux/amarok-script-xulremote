%define		scriptname	xulremote
Summary:	Control amaroK from any Firefox browser on your network
Summary(pl.UTF-8):	Sterowanie amaroKiem z dowolnej przeglądarki Firefox w sieci
Name:		amarok-script-%{scriptname}
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/xul-amarok/xulremote-%{version}.amarokscript.tar.gz
# Source0-md5:	6f0ceb519bf9e91ce6785610a75680a1
URL:		http://kde-apps.org/content/show.php?content=23630
BuildRequires:	sed >= 4.0
Requires:	amarok > 1.3
Requires:	kdebindings-python-dcop
Requires:	python >= 2.3
Requires:	python-PyQt
Suggests:	mozilla-firefox >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir %{_datadir}/apps/amarok/scripts

%description
An Firefox extension to use amaroK from your network. You can control
the player, browse your collection and manage the playlist.

AmaroK XUL Remote is an amaroK script that allows you to control
amaroK from any Firefox browser on your network.

To install the Firefox extension, open in Firefox
<http://amarok_host:8888/>, and install the extension.

%description -l pl.UTF-8
Rozszerzenie Firefoksa do używania amaroKa z sieci. Pozwala sterować
odtwarzaczem, przeglądać kolekcję muzyki i zarządzać listą
odtwarzania.

AmaroK XUL Remote to skrypt amaroKa pozwalający na sterowanie
amaroKiem z dowolnej przeglądarki Firefox w sieci.

Aby zainstalować rozszerzenie Firefoksa, należy otworzyć w Firefoksie
adres <http://host_z_amarokiem:8888/> i zainstalować rozszerzenie.

%prep
%setup -q -n %{scriptname}
%{__sed} -i -e 's,\r$,,' README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_scriptdir}/%{scriptname},%{_xuldir}}
cp -a . $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_scriptdir}/%{scriptname}
# README must be here in %files, not in %doc
%{_scriptdir}/%{scriptname}/README
%{_scriptdir}/%{scriptname}/Changelog

%{_scriptdir}/%{scriptname}/*.spec
%{_scriptdir}/%{scriptname}/*.ui
%{_scriptdir}/%{scriptname}/*.xpi
%{_scriptdir}/%{scriptname}/Amarok.py
%{_scriptdir}/%{scriptname}/AmarokHTTPServer.py
%{_scriptdir}/%{scriptname}/XULremoteConfigDialog.py

# Do not mark any other file executable than the main script as amarok thinks
# it's a plugin frontend.
%attr(755,root,root) %{_scriptdir}/%{scriptname}/XulRemote.py
