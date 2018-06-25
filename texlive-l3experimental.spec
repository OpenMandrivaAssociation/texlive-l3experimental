Name:		texlive-l3experimental
Version:	20180514
Release:	1
Summary:	Experimental LaTeX3 concepts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3experimental
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The l3experimental packages are a collection of experimental
implementations for aspects of the LaTeX3 kernel, dealing with
higher-level ideas such as the Designer Interface. Some of them
work as stand alone packages, providing new functionality, and
can be used on top of LaTeX2e with no changes to the existing
kernel. The present release includes: xgalley, which controls
boxes receiving text for typesetting. l3regex: kernel support
for regular expression search and replace operations; l3sort:
kernel support for sorting sequences, token lists or comma-
lists, according to user-specified comparison criteria; l3str:
kernel support for string manipulation; l3tl-build: kernel
support for token list building; l3tl_analysis: kernel support
for token list analysis; and xcoffins, which allows the
alignment of boxes using a series of 'handle' positions,
supplementing the simple TeX reference point. All the files of
the bundle are also available in the Subversion (SVN)
repository of the LaTeX3 Project. The bundle on CTAN is based
on a snapshot of the SVN repository on 2013-10-11.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/l3experimental
%doc %{_texmfdistdir}/doc/latex/l3experimental
#- source
%doc %{_texmfdistdir}/source/latex/l3experimental

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
