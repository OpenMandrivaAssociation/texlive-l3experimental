# revision 24820
# category Package
# catalog-ctan /macros/latex/contrib/l3experimental
# catalog-date 2011-12-10 15:22:24 +0100
# catalog-license lppl1.3
# catalog-version SVN 3036
Name:		texlive-l3experimental
Version:	SVN3036
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
kernel. The present release includes: - l3galley: kernel
support for xgalley; - l3str: kernel support for string
manipulation; - l3regex kernel support for regular expression
search and replace operations; - xcoffins, which allows the
alignment of boxes using a series of 'handle' positions,
supplementing the simple TeX reference point; and - xgalley,
which controls boxes receiving text for typesetting. All the
files of the bundle are also available in the Subversion (SVN)
repository of the LaTeX3 Project. The bundle on CTAN is based
on a snapshot of the SVN repository on 2011-11-19.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3regex.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-hex.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88591.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso885910.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso885911.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso885913.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso885914.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso885915.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso885916.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88592.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88593.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88594.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88595.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88596.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88597.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88598.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-iso88599.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-name.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-string.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-url.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-utf16.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-utf32.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-utf8.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str.sty
%{_texmfdistdir}/tex/latex/l3experimental/xcoffins/xcoffins.sty
%{_texmfdistdir}/tex/latex/l3experimental/xgalley/l3galley.sty
%{_texmfdistdir}/tex/latex/l3experimental/xgalley/xgalley.sty
%doc %{_texmfdistdir}/doc/latex/l3experimental/README
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3regex.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xcoffins/xcoffins.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xgalley/l3galley.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xgalley/xgalley.pdf
#- source
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3regex.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3str.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3str.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/xcoffins/xcoffins.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xcoffins/xcoffins.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/l3galley.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/xgalley.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/xgalley.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
