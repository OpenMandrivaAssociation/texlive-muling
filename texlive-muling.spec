Name:		texlive-muling
Version:	66741
Release:	1
Summary:	MA Thesis class for the Department of Linguistics, University of Mumbai
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/muling
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muling.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muling.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muling.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a class file for writing MA thesis as required by the
Department of Linguistics at the University of Mumbai.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/muling
%{_texmfdistdir}/tex/latex/muling
%doc %{_texmfdistdir}/doc/latex/muling

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
