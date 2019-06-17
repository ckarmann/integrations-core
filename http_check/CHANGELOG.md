# CHANGELOG - http_check

## 4.0.0 / 2019-05-14

* [Changed] Remove every default header except `User-Agent`. See [#3644](https://github.com/DataDog/integrations-core/pull/3644).
* [Added] Adhere to code style. See [#3516](https://github.com/DataDog/integrations-core/pull/3516).

## 3.2.1 / 2019-03-29

* [Fixed] Fix Python 3.7 support. See [#3293](https://github.com/DataDog/integrations-core/pull/3293).
* [Fixed] ensure_unicode with normalize for py3 compatibility. See [#3218](https://github.com/DataDog/integrations-core/pull/3218).

## 3.2.0 / 2019-02-18

* [Added] Add url as tag. See [#3080](https://github.com/DataDog/integrations-core/pull/3080).
* [Added] [http_check] adds instance tag to metrics. See [#3065](https://github.com/DataDog/integrations-core/pull/3065).

## 3.1.1 / 2018-12-07

* [Fixed] Fix unicode handling of log messages. See [#2700][1].

## 3.1.0 / 2018-11-30

* [Added] Add option to set `stream` parameter on requests. See [#2658][2]. Thanks [syskill][3].
* [Added] Upgrade cryptography. See [#2659][4].
* [Added] Upgrade requests. See [#2481][5].
* [Fixed] Use raw string literals when \ is present. See [#2465][6].
* [Added] Fix unicode handling on A6. See [#2435][7].
* [Added] Validate that the url starts with the scheme. See [#2393][8].

## 3.0.0 / 2018-10-12

* [Added] Handle SSL exception and send a DOWN service check status. See [#2332][9].
* [Changed] Refactoring: isolate config parsing. See [#2321][10].

## 2.4.0 / 2018-10-01

* [Fixed] Fix fetching ca_certs from init_config. See [#2318][11].
* [Added] Allow configuring cert expiration time in seconds. See [#2290][12].

## 2.3.0 / 2018-09-04

* [Fixed] Update cryptography to 2.3. See [#1927][13].
* [Fixed] fix link in config option description. See [#1865][14].
* [Added] support NTLM auth. See [#1812][15].
* [Fixed] Add data files to the wheel package. See [#1727][16].

## 2.2.0 / 2018-06-20

* [Fixed] Add support client auth for http check cert expiration.. See [#1754][17].
* [Fixed] Check will now send data with PUT, DELETE, and PATCH methods--not just POST. See [#1718][18].

## 2.1.0 / 2018-06-06

* [Fixed] fixes AttributeError when running on 6.2.1. See [#1617][19].
* [Fixed] Suppress InsecureRequestWarning for urllib3 for http_check. See [#1574][20].
* [Added] Allow users to disable matching hostnames verification in ssl cert verification. See [#1519][21].
* [Changed] Emit a warning if disable_ssl_validation is unset. See [#1517][22].

## 2.0.1 / 2018-05-11

* [BUGFIX] Properly detect default certificate file for all supported Platforms. See [#1340][23]

## 2.0.0 / 2018-03-23

* [BUGFIX] Make import of default certificate file relative rather than absolute
  Fixes loading problem on Windows, and/or allows check to be installed in other
  location
* [DEPRECATION] Remove the `skip_event` option from the check. See [#1054][24]

## 1.4.0 / 2018-02-13

* [IMPROVEMENT] begin deprecation of `no_proxy` config flag in favor of `skip_proxy`. See [#1057][25].

## 1.3.1 / 2018-01-17

* [BUGFIX] Use lowercase in an `if statement` for a user defined HTTP method.

## 1.3.0 / 2018-01-10

* [FEATURE] Report http connect status as metrics. See #659.
* [BUGFIX] User-defined "url" tag replaces default "url" tag. See[#301][26]. (Thanks [@colinmollenhour][27])
* [FEATURE] Add configurable ssl server name for cert expiration check. See[#905][28].

## 1.2.0 / 2017-10-10

* [FEATURE] Add support for client side certificate. See[#688][29]. (Thanks [@xkrt][30])
* [IMPROVEMENT] Make tornado optional. See [#758][31].

## 1.1.2 / 2017-08-28

* [IMPROVEMENT] Improved logging. See [#652][32].

## 1.1.1 / 2017-07-18

* [BUGFIX] Fix response tuple arity in SSL certificate check. See[#461][33].

## 1.1.0 / 2017-06-05

* [FEATURE] Add support for SOAP requests. See [#328][34].
* [FEATURE] Add gauge metric for ssl days left. See [#249][35].

## 1.0.0 / 2017-03-22

* [FEATURE] adds http_check integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2700
[2]: https://github.com/DataDog/integrations-core/pull/2658
[3]: https://github.com/syskill
[4]: https://github.com/DataDog/integrations-core/pull/2659
[5]: https://github.com/DataDog/integrations-core/pull/2481
[6]: https://github.com/DataDog/integrations-core/pull/2465
[7]: https://github.com/DataDog/integrations-core/pull/2435
[8]: https://github.com/DataDog/integrations-core/pull/2393
[9]: https://github.com/DataDog/integrations-core/pull/2332
[10]: https://github.com/DataDog/integrations-core/pull/2321
[11]: https://github.com/DataDog/integrations-core/pull/2318
[12]: https://github.com/DataDog/integrations-core/pull/2290
[13]: https://github.com/DataDog/integrations-core/pull/1927
[14]: https://github.com/DataDog/integrations-core/pull/1865
[15]: https://github.com/DataDog/integrations-core/pull/1812
[16]: https://github.com/DataDog/integrations-core/pull/1727
[17]: https://github.com/DataDog/integrations-core/pull/1754
[18]: https://github.com/DataDog/integrations-core/pull/1718
[19]: https://github.com/DataDog/integrations-core/pull/1617
[20]: https://github.com/DataDog/integrations-core/pull/1574
[21]: https://github.com/DataDog/integrations-core/pull/1519
[22]: https://github.com/DataDog/integrations-core/pull/1517
[23]: https://github.com/DataDog/integrations-core/pull/1340
[24]: https://github.com/DataDog/integrations-core/pull/1054
[25]: 
[26]: 
[27]: 
[28]: https://github.com/DataDog/integrations-core/pull/905
[29]: https://github.com/DataDog/integrations-core/issues/688
[30]: https://github.com/xkrt
[31]: https://github.com/DataDog/integrations-core/issues/758
[32]: https://github.com/DataDog/integrations-core/issues/652
[33]: https://github.com/DataDog/integrations-core/issues/461
[34]: https://github.com/DataDog/integrations-core/issues/328
[35]: https://github.com/DataDog/integrations-core/issues/249