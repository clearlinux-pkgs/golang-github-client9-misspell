Name     : golang-github-client9-misspell
Version  : 940f19ff686fdd0ee8395209994d4e243cb81e37
Release  : 3
URL      : https://github.com/client9/misspell/archive/940f19ff686fdd0ee8395209994d4e243cb81e37.tar.gz
Source0  : https://github.com/client9/misspell/archive/940f19ff686fdd0ee8395209994d4e243cb81e37.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-github-client9-gospell
BuildRequires : golang-googlecode-go-net

Requires : golang-github-client9-misspell-bin 

%description
[![Build Status](https://travis-ci.org/client9/misspell.svg?branch=master)](https://travis-ci.org/client9/misspell) [![Go Report Card](http://goreportcard.com/badge/client9/misspell)](http://goreportcard.com/report/client9/misspell) [![GoDoc](https://godoc.org/github.com/client9/misspell?status.svg)](https://godoc.org/github.com/client9/misspell) [![Coverage](http://gocover.io/_badge/github.com/client9/misspell)](http://gocover.io/github.com/client9/misspell) [![license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://raw.githubusercontent.com/client9/misspell/master/LICENSE)

%package bin
Summary: bin components for the golang-github-client9-misspell package.
Group: Binaries

%description bin
bin components for the golang-github-client9-misspell package.

%prep
%setup -q -n misspell-940f19ff686fdd0ee8395209994d4e243cb81e37

%build
export LANG=C
mkdir -p build-dir/src/github.com/client9
ln -s $(pwd) build-dir/src/github.com/client9/misspell
export GOPATH=$(pwd)/build-dir:/usr/lib/golang
pushd build-dir
for cmd in \
    genwords \
    misspell
do
    go build github.com/client9/misspell/cmd/$cmd
done
popd

%install
rm -rf %{buildroot}
%global gopath /usr/lib/golang
%global library_path github.com/client9/misspell
mkdir -p %{buildroot}/usr/bin

install -p -m 755 build-dir/genwords %{buildroot}/usr/bin
install -p -m 755 build-dir/misspell %{buildroot}/usr/bin


install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
     cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH="%{buildroot}%{gopath}"
go test -v -x %{library_path}

%files bin
%defattr(-,root,root,-)
/usr/bin/genwords
/usr/bin/misspell

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/client9/misspell/cmd/genwords/additions.go
/usr/lib/golang/src/github.com/client9/misspell/cmd/genwords/american.go
/usr/lib/golang/src/github.com/client9/misspell/cmd/genwords/delimit.go
/usr/lib/golang/src/github.com/client9/misspell/cmd/genwords/main.go
/usr/lib/golang/src/github.com/client9/misspell/cmd/genwords/wikipedia.go
/usr/lib/golang/src/github.com/client9/misspell/cmd/misspell/main.go
/usr/lib/golang/src/github.com/client9/misspell/falsepositives_test.go
/usr/lib/golang/src/github.com/client9/misspell/replace.go
/usr/lib/golang/src/github.com/client9/misspell/replace_test.go
/usr/lib/golang/src/github.com/client9/misspell/words.go
