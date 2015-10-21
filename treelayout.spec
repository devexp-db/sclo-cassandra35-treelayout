%global core org.abego.treelayout
Name:          treelayout
Version:       1.0.2
Release:       3%{?dist}
Summary:       Efficient and customizable Tree Layout Algorithm in Java
License:       BSD
URL:           http://treelayout.sourceforge.net/
Source0:       https://github.com/abego/treelayout/archive/v%{version}.tar.gz
Source1:       %{name}-project-pom.xml

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch

%description
Efficiently create compact, highly customizable
tree layouts. The software builds tree layouts
in linear time. I.e. even trees with many nodes
are built fast.

%package demo
Summary:       TreeLayout Core Demo

%description demo
Demo for "org.abego.treelayout.core".

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml
# Use org.netbeans.api:org-netbeans-api-visual:RELEASE67
%pom_disable_module %{core}.netbeans
%pom_disable_module %{core}.netbeans.demo

cp -p %{core}/CHANGES.txt .
cp -p %{core}/src/LICENSE.TXT .

native2ascii -encoding UTF8 %{core}/src/main/java/org/abego/treelayout/package-info.java \
 %{core}/src/main/java/org/abego/treelayout/package-info.java

%mvn_package :%{core}.project __noinstall

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{core}.core
%doc CHANGES.txt
%license LICENSE.TXT

%files demo -f .mfiles-%{core}.demo
%doc %{core}.demo/CHANGES.txt
%license %{core}.demo/src/LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%license LICENSE.TXT

%changelog
* Wed Oct 21 2015 gil cattaneo <puntogil@libero.it> 1.0.2-3
- use upstream source archive
- remove duplicate file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 24 2015 gil cattaneo <puntogil@libero.it> 1.0.2-1
- update to 1.0.2

* Sun Oct 06 2013 gil cattaneo <puntogil@libero.it> 1.0.1-1
- initial rpm
