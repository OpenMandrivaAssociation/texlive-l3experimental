%global tl_name l3experimental
%global tl_revision 79407

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Experimental LaTeX3 concepts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/l3experimental
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(l3kernel)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The l3experimental packages are a collection of experimental
implementations for aspects of the LaTeX3 kernel, dealing with higher-
level ideas such as the Designer Interface. Some of them work as stand
alone packages, providing new functionality, and can be used on top of
LaTeX2e with no changes to the existing kernel. The present release
includes: l3draw, a code-level interface for constructing drawings;
xcoffins, which allows the alignment of boxes using a series of 'handle'
positions, supplementing the simple TeX reference point;

