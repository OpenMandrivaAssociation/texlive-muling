%global tl_name muling
%global tl_revision 66741

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	MA Thesis class for the Department of Linguistics, University of Mumbai
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/muling
License:	gpl3+ fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/muling.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/muling.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/muling.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a class file for writing MA thesis as required by the Department
of Linguistics at the University of Mumbai.

