#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-multi_xml
Version  : 0.5.5
Release  : 4
URL      : https://rubygems.org/downloads/multi_xml-0.5.5.gem
Source0  : https://rubygems.org/downloads/multi_xml-0.5.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-docile
BuildRequires : rubygem-domain_name
BuildRequires : rubygem-http-cookie
BuildRequires : rubygem-mime-types
BuildRequires : rubygem-netrc
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rest-client
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html
BuildRequires : rubygem-term-ansicolor
BuildRequires : rubygem-thor
BuildRequires : rubygem-tins
BuildRequires : rubygem-unf
BuildRequires : rubygem-unf_ext

%description
# MultiXML
[![Gem Version](https://badge.fury.io/rb/multi_xml.png)][gem]
[![Build Status](https://secure.travis-ci.org/sferik/multi_xml.png?branch=master)][travis]
[![Dependency Status](https://gemnasium.com/sferik/multi_xml.png?travis)][gemnasium]
[![Code Climate](https://codeclimate.com/github/sferik/multi_xml.png)][codeclimate]
[![Coverage Status](https://coveralls.io/repos/sferik/multi_xml/badge.png?branch=master)][coveralls]

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n multi_xml-0.5.5
gem spec %{SOURCE0} -l --ruby > rubygem-multi_xml.gemspec

%build
gem build rubygem-multi_xml.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
multi_xml-0.5.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/multi_xml-0.5.5
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/multi_xml-0.5.5.gem
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/DisallowedTypeError/cdesc-DisallowedTypeError.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/DisallowedTypeError/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/FileLike/cdesc-FileLike.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/ParseError/cdesc-ParseError.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Libxml/cdesc-Libxml.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Libxml2Parser/cdesc-Libxml2Parser.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Nokogiri/cdesc-Nokogiri.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/append-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/attr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/cdata-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/cdesc-Handler.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/doc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/end_element-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/stack-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/start_element-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/Handler/text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Ox/cdesc-Ox.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/Rexml/cdesc-Rexml.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/Parsers/cdesc-Parsers.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/cdesc-MultiXml.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/default_parser-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/parse-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/parse_file-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/parser%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/parser-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/symbolize_keys-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/typecast_xml_value-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/MultiXml/undasherize_keys-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/REXML/cdesc-REXML.ri
/usr/lib64/ruby/gems/2.2.0/doc/multi_xml-0.5.5/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/LICENSE.md
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/README.md
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/.last_run.json
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/.resultset.json
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/.resultset.json.lock
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/application.css
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/application.js
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/colorbox/border.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/colorbox/controls.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/colorbox/loading.gif
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/colorbox/loading_background.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/favicon_green.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/favicon_red.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/favicon_yellow.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/loading.gif
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/magnify.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-bg_flat_0_aaaaaa_40x100.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-bg_flat_75_ffffff_40x100.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_55_fbf9ee_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_65_ffffff_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_75_dadada_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_75_e6e6e6_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_95_fef1ec_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-bg_highlight-soft_75_cccccc_1x100.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-icons_222222_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-icons_2e83ff_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-icons_454545_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-icons_888888_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/assets/0.10.0/smoothness/images/ui-icons_cd0a0a_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/coverage/index.html
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/lib/multi_xml.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/lib/multi_xml/parsers/libxml.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/lib/multi_xml/parsers/libxml2_parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/lib/multi_xml/parsers/nokogiri.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/lib/multi_xml/parsers/ox.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/lib/multi_xml/parsers/rexml.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/lib/multi_xml/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/multi_xml.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/spec/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/spec/multi_xml_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/spec/parser_shared_example.rb
/usr/lib64/ruby/gems/2.2.0/gems/multi_xml-0.5.5/spec/speed.rb
/usr/lib64/ruby/gems/2.2.0/specifications/multi_xml-0.5.5.gemspec
