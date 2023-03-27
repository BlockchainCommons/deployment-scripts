# Blockchain Commons Deployment Scripts

<!--Guidelines: https://github.com/BlockchainCommons/secure-template/wiki -->

### _by Nicholas Ochiel_

**Deployment Scripts** contains scripts used to run blockchain services at Blockchain Commons.

## List of files
- `/etc/nagios4`: Configuration for nagios4 monitoring. 
  - Nagios configuration reference can be found here: https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/toc.html.

### Also See

Also see our standard Bitcoin setup with [Bitcoin Standup Scripts](https://github.com/BlockchainCommons/Bitcoin-Standup-Scripts).

## Installation Instructions

- [Install Linode's LongView](https://www.linode.com/docs/guides/monitor-and-configure-nagios-alerts-on-debian-10-ubuntu-2004/#install-email-services)
- [Install Nagios on Linode](https://www.linode.com/docs/products/tools/monitoring/developers/)
- [Install Tor](https://support.torproject.org/apt/#apt_tor-deb-repo)

## Usage Instructions

**NB: Do not commit any credentials to this repository.** Any credentials/keys should be configured as `$USER` variables in etc\nagios4\resource.cfg. We use the following:
- `$USER2`: Tor proxy port.
- `$USER3`: Username for BlockckainCommons Bitcoin RPC.
- `$USER4`: RPC auth password generated using https://github.com/bitcoin/bitcoin/blob/master/share/rpcauth/rpcauth.py.

### Nagios 
- Define hosts to be monitored in: etc\nagios4\servers\servers.cfg
#### Nagios email notifications
- List contact details in etc\nagios4\objects\contacts.cfg.
- There are several alternative setups for email notifications:
    - [Using Gmail](https://www.linode.com/docs/guides/configure-postfix-to-send-mail-using-gmail-and-google-workspace-on-debian-or-ubuntu/)
    - [Using external SMTP](https://www.linode.com/docs/guides/postfix-smtp-debian7/)
    - [Run a Linode mail-server on a subdomain](https://www.linode.com/docs/guides/running-a-mail-server/#sending-email-on-linode)
    - Modify any `notify-host-by-email` `command` directives in `etc/nagios4/commands.cfg` to use the settings you have configured for sending email.

#### Nagios monitoring of Tor services
- The hostname for a Tor hidden service is read using: `cat /var/lib/tor/$HOSTNAME/hostname`
- Modify any `service.check_command` directives to use the `check_http! -p $USER2` to monitor hidden services.
    - `$USER2` is a variable configured in etc\nagios4\resource.cfg.

## Status 

`deployment-scripts` is used for installing and maintaining BlockchainCommons infrastructure and so it's under continuous development.

### Dependencies

To use `deployment-scripts` you'll need to use the following tools:

- A Debian Linode VPS.
- Nagios4.
- Tor

## Financial Support

`deployment-scripts` is a project of [Blockchain Commons](https://www.blockchaincommons.com/). We are proudly a "not-for-profit" social benefit corporation committed to open source & open development. Our work is funded entirely by donations and collaborative partnerships with people like you. Every contribution will be spent on building open tools, technologies, and techniques that sustain and advance blockchain and internet security infrastructure and promote an open web.

To financially support further development of `deployment-scripts` and other projects, please consider becoming a Patron of Blockchain Commons through ongoing monthly patronage as a [GitHub Sponsor](https://github.com/sponsors/BlockchainCommons). You can also support Blockchain Commons with bitcoins at our [BTCPay Server](https://btcpay.blockchaincommons.com/).

## Contributing

We encourage public contributions through issues and pull requests! Please review [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our development process. All contributions to this repository require a GPG signed [Contributor License Agreement](./CLA.md).

### Discussions

The best place to talk about Blockchain Commons and its projects is in our GitHub Discussions areas.

[**Gordian Developer Community**](https://github.com/BlockchainCommons/Gordian-Developer-Community/discussions). For standards and open-source developers who want to talk about interoperable wallet specifications, please use the Discussions area of the [Gordian Developer Community repo](https://github.com/BlockchainCommons/Gordian-Developer-Community/discussions). This is where you talk about Gordian specifications such as [Gordian Envelope](https://github.com/BlockchainCommons/Gordian/tree/master/Envelope#articles), [bc-shamir](https://github.com/BlockchainCommons/bc-shamir), [Sharded Secret Key Reconstruction](https://github.com/BlockchainCommons/bc-sskr), and [bc-ur](https://github.com/BlockchainCommons/bc-ur) as well as the larger [Gordian Architecture](https://github.com/BlockchainCommons/Gordian/blob/master/Docs/Overview-Architecture.md), its [Principles](https://github.com/BlockchainCommons/Gordian#gordian-principles) of independence, privacy, resilience, and openness, and its macro-architectural ideas such as functional partition (including airgapping, the original name of this community).

[**Gordian User Community**](https://github.com/BlockchainCommons/Gordian/discussions). For users of the Gordian reference apps, including [Gordian Coordinator](https://github.com/BlockchainCommons/iOS-GordianCoordinator), [Gordian Seed Tool](https://github.com/BlockchainCommons/GordianSeedTool-iOS), [Gordian Server](https://github.com/BlockchainCommons/GordianServer-macOS), [Gordian Wallet](https://github.com/BlockchainCommons/GordianWallet-iOS), and [SpotBit](https://github.com/BlockchainCommons/spotbit) as well as our whole series of [CLI apps](https://github.com/BlockchainCommons/Gordian/blob/master/Docs/Overview-Apps.md#cli-apps). This is a place to talk about bug reports and feature requests as well as to explore how our reference apps embody the [Gordian Principles](https://github.com/BlockchainCommons/Gordian#gordian-principles).

[**Blockchain Commons Discussions**](https://github.com/BlockchainCommons/Community/discussions). For developers, interns, and patrons of Blockchain Commons, please use the discussions area of the [Community repo](https://github.com/BlockchainCommons/Community) to talk about general Blockchain Commons issues, the intern program, or topics other than those covered by the [Gordian Developer Community](https://github.com/BlockchainCommons/Gordian-Developer-Community/discussions) or the 
[Gordian User Community](https://github.com/BlockchainCommons/Gordian/discussions).

### Other Questions & Problems

As an open-source, open-development community, Blockchain Commons does not have the resources to provide direct support of our projects. Please consider the discussions area as a locale where you might get answers to questions. Alternatively, please use this repository's [issues](./issues) feature. Unfortunately, we can not make any promises on response time.

If your company requires support to use our projects, please feel free to contact us directly about options. We may be able to offer you a contract for support from one of our contributors, or we might be able to point you to another entity who can offer the contractual support that you need.

### Credits

The following people directly contributed to this repository. You can add your name here by getting involved. The first step is learning how to contribute from our [CONTRIBUTING.md](./CONTRIBUTING.md) documentation.

| Name              | Role                | Github                                            | Email                                 | GPG Fingerprint                                    |
| ----------------- | ------------------- | ------------------------------------------------- | ------------------------------------- | -------------------------------------------------- |
| Christopher Allen | Principal Architect | [@ChristopherA](https://github.com/ChristopherA) | \<ChristopherA@LifeWithAlacrity.com\> | FDFE 14A5 4ECB 30FC 5D22  74EF F8D3 6C91 3574 05ED |
| Nicholas Ochiel   | Site Reliability Engineering          | [@nochiel](https://github.com/nochiel) | \<nochiel@users.noreply.github.com\> | 45EA 5C81 9B7E E915 C2A2 7C64 4444 1190 7BE8 83D9 |

## Responsible Disclosure

We want to keep all of our software safe for everyone. If you have discovered a security vulnerability, we appreciate your help in disclosing it to us in a responsible manner. We are unfortunately not able to offer bug bounties at this time.

We do ask that you offer us good faith and use best efforts not to leak information or harm any user, their data, or our developer community. Please give us a reasonable amount of time to fix the issue before you publish it. Do not defraud our users or us in the process of discovery. We promise not to bring legal action against researchers who point out a problem provided they do their best to follow the these guidelines.

### Reporting a Vulnerability

Please report suspected security vulnerabilities in private via email to ChristopherA@BlockchainCommons.com (do not use this email for support). Please do NOT create publicly viewable issues for suspected security vulnerabilities.

The following keys may be used to communicate sensitive information to developers:

| Name              | Fingerprint                                        |
| ----------------- | -------------------------------------------------- |
| Christopher Allen | FDFE 14A5 4ECB 30FC 5D22  74EF F8D3 6C91 3574 05ED |

You can import a key by running the following command with that individual’s fingerprint: `gpg --recv-keys "<fingerprint>"` Ensure that you put quotes around fingerprints that contain spaces.
