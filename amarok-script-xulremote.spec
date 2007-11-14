%define		scriptname	xulremote
Summary:	Control amaroK from any Firefox browser on your network
Name:		amarok-script-%{scriptname}
Version:	1.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/xul-amarok/xulremote-%{version}.amarokscript.tar.gz
# Source0-md5:	6f0ceb519bf9e91ce6785610a75680a1
URL:		http://linux.softpedia.com/get/Multimedia/Audio/amaroK-Scripts/amaroK-XUL-Remote-9555.shtml
BuildRequires:	sed >= 4.0
Requires:	amarok > 1.3
Requires:	kdebindings-python-dcop
Requires:	python >= 2.3
Requires:	python-PyQt
# Requires: Firefox deer park (tested 1.5 beta1)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir %{_datadir}/apps/amarok/scripts
#%define		_xuldir		%{_datadir}/xulrunner
%define		_xuldir		%{_scriptdir}/%{scriptname}/xul

%description
An Firefox extension to use amaroK from your network. You can control
the player, browse your collection and manage the playlist.

AmaroK XUL Remote is an amaroK script that allows you to control
amaroK from any Firefox browser on your network.

%prep
%setup -q -n %{scriptname}
%{__sed} -i -e 's,\r$,,' README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_scriptdir}/%{scriptname},%{_xuldir}}
cp -a *.py *.ui XulRemote.spec $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}
cp -a README Changelog $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}
cp -a xul-amarok.xpi $RPM_BUILD_ROOT%{_xuldir}

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
%attr(755,root,root) %{_scriptdir}/%{scriptname}/*.py
#%attr(755,root,root) %{_scriptdir}/%{scriptname}/*.sh

%{_xuldir}
