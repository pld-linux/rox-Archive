%define _name Archive
Summary:	ROX-archive is a program for creating and extracting archives
Summary(pl):	ROX-archive s³u¿y do tworzenia i dekompresji archiwów
Name:		rox-%{_name}
Version:	1.9.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/archive-%{version}.tgz
# Source0-md5:	3acb95461a0e95f3bdcd0aca9470925d
URL:		http://rox.sourceforge.net/archive.php3
Requires:	python-pygtk-gtk
Requires:	rox >= 2.2.0-2
Requires:	rox-Lib2
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-archive is a very easy to use program for creating and extracting
archives. You can use this program to compress a directory or file
into a single, smaller file (which can be stored, emailed, etc).

%description -l pl
ROX-archive jest bardzo prostym w u¿yciu programem s³u¿±cym do
tworzenia i dekompresji archiwów. Ten program mo¿esz u¿ywaæ aby
spakowaæ katalog lub plik do jednego, mniejszego (który mo¿e byæ
przechowywany, wys³any poczt±, itp.)

%prep
%setup -q -n archive-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,Messages}

cd Archive
install .DirIcon App* *.py $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install Messages/*.gmo $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Messages

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Archive/Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%dir %{_appsdir}/%{_name}
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/*.py[co]
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}/Messages
%lang(de) %{_appsdir}/%{_name}/Messages/de.gmo
%lang(es) %{_appsdir}/%{_name}/Messages/es.gmo
%lang(it) %{_appsdir}/%{_name}/Messages/it.gmo
%lang(zh_CN) %{_appsdir}/%{_name}/Messages/zh_CN.gmo
%lang(zh_TW) %{_appsdir}/%{_name}/Messages/zh_TW.gmo
