var gentooSchema =
{
    "type": "object",
    "properties": {
        "interface": {
            "type": "string",
            "title": "Interface",
            "description": "<div class='formlabel'>Network interface</div>",
            "required": true
        },
        "host": {
            "type": "string",
            "title": "Host",
            "description": "<div class='formlabel'>Host that installation server should run on</div>",
            "required": true
        },
        "port": {
            "type": "integer",
            "title": "Port",
            "description": "<div class='formlabel'>Port for installation server</div>",
            "required": true
        },
        "auth": {
            "type": "string",
            "title": "Auth",
            "length": "4"
        },
        "autosave_config": {
            "type": "boolean",
            "title": "Autosave Config",
            "description": "<div class='formlabel'>Autosave Configuration</div>"
        },
        "sync_time": {
            "type": "boolean",
            "title": "Sync Time",
            "description": "<div class='formlabel'></div>"
        },
        "dev": {
            "type": "array",
            "title": "Dev",
            "default": [],
            "items": {
                "type": "object",
                "title": "Dev",
                "properties": {
                    "disk": {
                        "type": "array",
                        "title": "Disks",
                        "description": "System Disks",
                        "default": [],
                        "items": {
                            "type": "object",
                            "title": "Disk",
                            "properties": {
                                "partition": {
                                    "type": "array",
                                    "minItems": 1,
                                    "title": "Partitions",
                                    "default": [],
                                    "items": {
                                        "type": "object",
                                        "title": "Partition",
                                        "properties": {
                                            "parttype": {
                                                "type": "string",
                                                "title": "Partition Type",
                                                "required": true
                                            },
                                            "mountpoint": {
                                                "type": "string",
                                                "title": "Mount Point",
                                                "required": true
                                            },
                                            "opts": {
                                                "type": "string",
                                                "title": "Options"
                                            },
                                            "dump": {
                                                "type": "boolean",
                                                "title": "Dump"
                                            },
                                            "pass": {
                                                "type": "boolean",
                                                "title": "Pass"
                                            }
                                        }
                                    }
                                },
                                "label": {
                                    "type": "string",
                                    "title": "Label"
                                }
                            }
                        }
                    }
                }
            }
        },
        "target": {
            "type": "object",
            "title": "Target",
            "properties": {
                "stage": {
                    "type": "string",
                    "title": "Stage"
                },
                "repo_snapshot": {
                    "type": "object",
                    "title": "Repo Snapshot",
                    "properties": {
                        "uri": {
                            "type": "string",
                            "title": "URI",
                            "required": true
                        },
                        "md5sum_uri": {
                            "type": "string",
                            "title": "MD5 Sum URI"
                        },
                        "gpgsig_uri": {
                            "type": "string",
                            "title": "GPG Sig URI"
                        }
                    }
                },
                "profile": {
                    "type": "string",
                    "title": "Profile"
                },
                "hostname": {
                    "type": "string",
                    "title": "Hostname"
                },
                "timezone": {
                    "type": "string",
                    "title": "Timezone"
                },
                "locales": {
                    "type": "array",
                    "minItems": 1,
                    "title": "Locales",
                    "default": [],
                    "items": {
                        "type": "string",
                        "title": "Locale",
                        "required": true
                    }
                },
                "kernel": {
                    "type": "object",
                    "title": "Kernel",
                    "properties": {
                        "package": {
                            "type": "string",
                            "title": "Kernel Package"
                        },
                        "config": {
                            "type": "string",
                            "title": "Kernel Config"
                        }
                    }
                },
                "bootloader": {
                    "type": "object",
                    "title": "Bootloader",
                    "properties": {
                        "bootloaderName": {
                            "type": "string",
                            "title": "Bootloader Name"
                        },
                        "platform": {
                            "type": "string",
                            "title": "Platform"
                        },
                        "target": {
                            "type": "string",
                            "title": "Target"
                        },
                        "efi-directory": {
                            "type": "string",
                            "title": "EFI Directory"
                        }
                    }
                },
                "portage": {
                    "type": "object",
                    "title": "Portage",
                    "properties": {
                        "sync": {
                            "type": "boolean",
                            "title": "Portage Sync"
                        },
                        "makeConf": {
                            "type": "object",
                            "title": "Make.Conf",
                            "properties": {
                                "cflags": {
                                    "type": "string",
                                    "title": "CFlags"
                                },
                                "cxxflags": {
                                    "type": "string",
                                    "title": "CXXFlags"
                                },
                                "chost": {
                                    "type": "string",
                                    "title": "CHost"
                                },
                                "makeopts": {
                                    "type": "string",
                                    "title": "MakeOpts"
                                },
                                "gentoo_mirrors": {
                                    "type": "string",
                                    "title": "Gentoo Mirrors"
                                },
                                "features": {
                                    "type": "string",
                                    "title": "Features"
                                },
                                "accept_license": {
                                    "type": "string",
                                    "title": "Accept License"
                                },
                                "accept_keywords": {
                                    "type": "string",
                                    "title": "Accept Keywords"
                                },
                                "use": {
                                    "type": "string",
                                    "title": "USE Flags"
                                },
                                "input_devices": {
                                    "type": "string",
                                    "title": "Input Devices"
                                },
                                "video_cards": {
                                    "type": "string",
                                    "title": "Video Cards"
                                }
                            }
                        },
                        "reposConf": {
                            "type": "object",
                            "title": "Repos.Conf",
                            "properties": {
                                "main_repo": {
                                    "type": "string",
                                    "title": "Main Repo"
                                },
                                "gentoo": {
                                    "type": "object",
                                    "title": "Gentoo",
                                    "properties": {
                                        "location": {
                                            "type": "string",
                                            "title": "Location"
                                        },
                                        "sync_type": {
                                            "type": "string",
                                            "title": "Sync Type"
                                        },
                                        "sync_uri": {
                                            "type": "string",
                                            "title": "Sync URI"
                                        },
                                        "auto_sync": {
                                            "type": "boolean",
                                            "title": "Auto Sync"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "users": {
                    "type": "array",
                    "title": "Users",
                    "default": [],
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "title": "User",
                        "properties": {
                            "username": {
                                "type": "string",
                                "title": "Username",
                                "required": true
                            },
                            "real_name": {
                                "type": "string",
                                "title": "Real Name",
                                "required": false
                            },
                            "email": {
                                "type": "string",
                                "title": "Email",
                                "required": false
                            },
                            "default_password": {
                                "type": "string",
                                "title": "Default Password",
                                "required": true
                            },
                            "reset_password_on_login": {
                                "type": "boolean",
                                "title": "Reset Password On Login",
                            },
                            "create_home": {
                                "type": "boolean",
                                "title": "Create Home",
                                "default": true
                            },
                            "groups": {
                                "type": "string",
                                "title": "Groups",
                                "required": false
                            }
                        }

                    }
                }
            }
        }

    }
}
