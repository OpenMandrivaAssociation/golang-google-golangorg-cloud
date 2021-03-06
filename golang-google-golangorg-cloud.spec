# Bootstrap needed to avoid circular dep
%bcond_without bootstrap
# Run tests in check
# Disabled for bootstrapping
%bcond_with check

# http://github.com/GoogleCloudPlatform/google-cloud-go
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
%global goipath         cloud.google.com/go
Version:                0.31.0

%gometa

Name:           golang-google-golangorg-cloud
Release:        1%{?dist}
Summary:        Google Cloud Platform APIs related types and common functions
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
%if %{with bootstrap}
Source1:        google-cloud-go-0.31.0-vendor.tar.gz
%endif

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%if %{without bootstrap}
BuildRequires: golang(github.com/golang/mock/gomock)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/ptypes)
BuildRequires: golang(github.com/golang/protobuf/ptypes/any)
BuildRequires: golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires: golang(github.com/google/btree)
BuildRequires: golang(github.com/google/go-cmp/cmp)
BuildRequires: golang(github.com/google/martian)
BuildRequires: golang(github.com/google/martian/fifo)
BuildRequires: golang(github.com/google/martian/httpspec)
BuildRequires: golang(github.com/google/martian/martianlog)
BuildRequires: golang(github.com/google/martian/mitm)
BuildRequires: golang(github.com/google/pprof/profile)
BuildRequires: golang(github.com/googleapis/gax-go)
BuildRequires: golang(golang.org/x/build/kubernetes)
BuildRequires: golang(golang.org/x/build/kubernetes/api)
BuildRequires: golang(golang.org/x/build/kubernetes/gke)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/oauth2/jwt)
BuildRequires: golang(golang.org/x/sync/errgroup)
BuildRequires: golang(golang.org/x/sync/semaphore)
BuildRequires: golang(golang.org/x/text/language)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(google.golang.org/api/bigquery/v2)
BuildRequires: golang(google.golang.org/api/cloudbuild/v1)
BuildRequires: golang(google.golang.org/api/clouddebugger/v2)
BuildRequires: golang(google.golang.org/api/cloudresourcemanager/v1)
BuildRequires: golang(google.golang.org/api/cloudtrace/v1)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(google.golang.org/api/container/v1)
BuildRequires: golang(google.golang.org/api/gensupport)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/iterator)
BuildRequires: golang(google.golang.org/api/option)
BuildRequires: golang(google.golang.org/api/storage/v1)
BuildRequires: golang(google.golang.org/api/support/bundler)
BuildRequires: golang(google.golang.org/api/transport)
BuildRequires: golang(google.golang.org/api/transport/grpc)
BuildRequires: golang(google.golang.org/api/transport/http)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/label)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/metric)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/monitoredres)
BuildRequires: golang(google.golang.org/genproto/googleapis/appengine/logging/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/bigtable/admin/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/bigtable/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/asset/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/audit)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/bigquery/datatransfer/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/dataproc/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/dataproc/v1beta2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/dialogflow/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/kms/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/language/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/language/v1beta2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/oslogin/common)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/oslogin/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/oslogin/v1beta)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/redis/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/redis/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/speech/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/speech/v1p1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/tasks/v2beta2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/tasks/v2beta3)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/texttospeech/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/videointelligence/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/videointelligence/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/videointelligence/v1beta2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/vision/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/vision/v1p1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/container/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/datastore/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/clouddebugger/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/cloudprofiler/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/cloudtrace/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/cloudtrace/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/containeranalysis/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/containeranalysis/v1beta1/grafeas)
BuildRequires: golang(google.golang.org/genproto/googleapis/firestore/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/iam/admin/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/iam/credentials/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/iam/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/logging/type)
BuildRequires: golang(google.golang.org/genproto/googleapis/logging/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/longrunning)
BuildRequires: golang(google.golang.org/genproto/googleapis/monitoring/v3)
BuildRequires: golang(google.golang.org/genproto/googleapis/privacy/dlp/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/pubsub/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/rpc/code)
BuildRequires: golang(google.golang.org/genproto/googleapis/rpc/errdetails)
BuildRequires: golang(google.golang.org/genproto/googleapis/rpc/status)
BuildRequires: golang(google.golang.org/genproto/googleapis/spanner/admin/database/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/spanner/admin/instance/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/spanner/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/type/latlng)
BuildRequires: golang(google.golang.org/genproto/protobuf/field_mask)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/keepalive)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/status)
%endif

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
%if %{with bootstrap}
%autosetup %{?forgesetupargs} -N -T -D -a 1
%endif

%install
%goinstall

%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS

%changelog
* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.31.0-1
- Update to release v0.31.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.21.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.21.0-1
- Update to v0.21.0
  Change import path prefix to cloud.google.com/go
  resolves: #1558755

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git872c736
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git872c736
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git872c736
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git872c736
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git872c736
- Bump to upstream 872c736f496c2ba12786bedbb8325576bbdb33cf
  related: #1246239

* Thu Dec 15 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git2400193
- Polish the spec file
  related: #1246239

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git2400193
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.git2400193
- Bump to upstream 2400193c85c3561d13880d34e0e10c4315bb02af
  related: #1246239

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git95c332f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git95c332f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git95c332f
- Update spec file to spec-2.0
  related: #1246239

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git95c332f
- Bump to upstream 95c332f94e6766fa122231c0a95ddf15ac26bf70
  resolves: #1246239

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git2e43671
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git1c3fdc5
- First package for Fedora
  resolves: #1185281
