Summary:	xmlmp facilitates authoring of Unix manpages using XML
Summary(pl.UTF-8):   xmlmp - narzędzie do tworzenia stron podręcznika z plików XML
Name:		xmlmp
Version:	1.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://efault.net/npat/hacks/xmlmp/dist/%{name}-%{version}.tar.gz
# Source0-md5:	e998cdc06d37e837e620586fef2e88f4
URL:		http://npat.efault.net/hacks/xmlmp/
BuildRequires:	python-devel >= 2.0.0
%pyrequires_eq  python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmlmp facilitates authoring of Unix manpages using XML. It defines 
the xmlmp 1.x DTD and provides filters that convert documents 
complying with it to either Unix manpages or HTML.

%description -l pl.UTF-8
xmlmp jest narzędziem do formatowania stron podręcznika z plików XML.
Zawiera DTD (Document Type Definition, czyli definicję typu dokumentu)
dla xmlmp 1.x i filtr konwertujący zgodny z nim dokument do strony 
podręcznika lub pliku HTML.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}
python setup.py install \
        --root=$RPM_BUILD_ROOT \
	--install-data=%{_datadir}
	
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{_mandir}/man1/*
