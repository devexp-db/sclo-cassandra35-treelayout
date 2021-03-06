%{?scl:%scl_package treelayout}
%{!?scl:%global pkg_name %{name}}

%global core org.abego.treelayout

Name:		%{?scl_prefix}treelayout
Version:	1.0.3
Release:	4%{?dist}
Summary:	Efficient and customizable Tree Layout Algorithm in Java
License:	BSD
URL:		http://treelayout.sourceforge.net/
Source0:	https://github.com/abego/%{pkg_name}/archive/v%{version}.tar.gz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:	%{?scl_prefix_maven}sonatype-oss-parent
BuildRequires:	%{?scl_prefix_java_common}junit
%{?scl:Requires: %scl_runtime}

BuildArch:	noarch

%description
Efficiently create compact, highly customizable
tree layouts. The software builds tree layouts
in linear time. I.e. even trees with many nodes
are built fast.

%package demo
Summary:	TreeLayout Core Demo

%description demo
Demo for "org.abego.treelayout.core".

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{pkg_name}-%{version}

# This is a dummy POM added just to ease building in the RPM platforms:
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <modelVersion>4.0.0</modelVersion>
  <groupId>org.abego.treelayout</groupId>
  <artifactId>org.abego.treelayout.project</artifactId>
  <packaging>pom</packaging>
  <version>%{version}</version>

  <modules>
    <module>org.abego.treelayout</module>
    <module>org.abego.treelayout.demo</module>
    <!-- Use org.netbeans.api:org-netbeans-api-visual:RELEASE67: -->
    <!--module>org.abego.treelayout.netbeans</module-->
    <!--module>org.abego.treelayout.netbeans.demo</module-->
  </modules>

</project>
EOF

# fix non ASCII chars
native2ascii -encoding UTF8 %{core}/src/main/java/org/abego/treelayout/package-info.java \
 %{core}/src/main/java/org/abego/treelayout/package-info.java

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_package :%{core}.project __noinstall
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build -s
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles-%{core}.core
%doc %{core}/CHANGES.txt README.md
%license %{core}/src/LICENSE.TXT

%files demo -f .mfiles-%{core}.demo
%doc %{core}.demo/CHANGES.txt
%license %{core}.demo/src/LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%license %{core}/src/LICENSE.TXT

%changelog
* Thu Dec 08 2016 Tomas Repik <trepik@redhat.com> - 1.0.3-4
- scl conversion

* Wed Jun 22 2016 gil cattaneo <puntogil@libero.it> 1.0.3-3
- regenerate build-requires

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 gil cattaneo <puntogil@libero.it> 1.0.3-1
- update to 1.0.3

* Wed Oct 21 2015 gil cattaneo <puntogil@libero.it> 1.0.2-3
- use upstream source archive
- remove duplicate file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 24 2015 gil cattaneo <puntogil@libero.it> 1.0.2-1
- update to 1.0.2

* Sun Oct 06 2013 gil cattaneo <puntogil@libero.it> 1.0.1-1
- initial rpm
