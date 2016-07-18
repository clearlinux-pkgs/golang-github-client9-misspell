Name     : golang-github-client9-misspell
Version  : 940f19ff686fdd0ee8395209994d4e243cb81e37
Release  : 1
URL      : https://github.com/client9/misspell/archive/940f19ff686fdd0ee8395209994d4e243cb81e37.tar.gz
Source0  : https://github.com/client9/misspell/archive/940f19ff686fdd0ee8395209994d4e243cb81e37.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go

%description
[![Build Status](https://travis-ci.org/client9/misspell.svg?branch=master)](https://travis-ci.org/client9/misspell) [![Go Report Card](http://goreportcard.com/badge/client9/misspell)](http://goreportcard.com/report/client9/misspell) [![GoDoc](https://godoc.org/github.com/client9/misspell?status.svg)](https://godoc.org/github.com/client9/misspell) [![Coverage](http://gocover.io/_badge/github.com/client9/misspell)](http://gocover.io/github.com/client9/misspell) [![license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://raw.githubusercontent.com/client9/misspell/master/LICENSE)

%prep
%setup -q -n misspell-940f19ff686fdd0ee8395209994d4e243cb81e37

%build
export LANG=C

%install
gopath="/usr/lib/golang"
library_path="github.com/client9/misspell"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x

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
