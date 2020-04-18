
old_data = [
	"7quYJgJceUJVjQZcdBtCp9c6oE4TLkDgxeT1mpKLLatVG9mNbqM",
	"7rnWv7CBL3Z8uoYQpDSU4PSrqZVBEryfrJYX9zKYoKQD3GX57Y2",
	"7rwNQ8kbh7XgaSFx8Ay7dFXMapznowzr2e9SHA5vcbVnPJvGwAj",
	"7rNqu9TAnZ6jQc1QJuSAwZk4mxtXSwnW85vksp4Mgg2yqWQZiuL",
	"7rxEqJPLbk1T89TNpeygZQFnXzDDeN8wEjQmSefqqevnoU142td",
	"7qnLWxKbN5Q27h5hK5dXH2hGAeRrd5fiscxPB8XqKrj8YFkdwii",
	"7qoUS6VM28HPBbJu1ZXofRH82M1zDdcmt5TtFZZkihN1tZ5Gwxb",
	"7r2r57oDTh127yhVWS6ZBGg6unvqGv1mxS7RG3xxkMJkWCfLxyS",
	"7sR5FaLAzTypzDyYKmu7hPqeVTvktpSaEbTamWdNgDFFThqXYq3",
	"7qbEsHNASJRUKZZQN5TkpiyMmwoZjEW4xpLuYLfk1SuD1CmR5qf",
	"7rnV5s8mM1RzZTHKoBxBLvBn93AGEYwfd7yjx7AB6nJkdfTPciq",
	"7sGHgK6KhMMQNLhnJaZFRnBGq38yeqVf3eBHBKftFn1arJWfroG",
	"7s2z1V4woHsoW4xJzKVcQezbKF4tgGKMouFZ2EtWBUjTh2S1DLg",
	"7rriqL1py3mDQ8Hz7yajCesKsH7swTAjtyMB7qG5zfowfZpg5sZ",
	"7sUJxemjtEe5VRhuFSuc7fnYdNsDSnorfqUo8MHef6BvzxzHo3f",
	"7rJGWLPRueGmL8SE4BCvSQqUnHe4Hj3prZG1daxfv6NhhAq3so9",
	"7s8muFtC7PsovYDdXxjawwZT5xVBDS6rePDcRjghppeuSPxVfmR",
	"7qs5C9CA8CefQRx47JA7SBePcDBxv3dt6owuA6HwLcHWeXGK2H6",
	"7sK3tr8KHL7vrN2m27VZWgNeCLNbet4EnB7TpmJHAKuptdUixpE",
	"7sNXdKoXBAFH6gbADrCxytbPhuQoGsvezSFCexBqfvXmLJKhopR",
	"7r7Z1Hx8i18XamA9cCRVRAzUsYED2YGjGixE6wFTgm46X9yaVQ1",
	"7rxa6wGGFnVKYHwxhyrJP83HRsrwyqmqs2vijjmFSWdaHqbemcN",
	"7qmVdc2hqtvw4pCJ83U9hsFxxSWULH4BF2ftPqNxgNJPwY3JSf3",
	"7r7xZsMmrXqTZFHmTFdeQGaidzUqaMvn8szy8JiSWiLh7nC6434",
	"7r9SsTroh2e3WZM3XKP5sTQubgjTYBj99PVHRC4NQuNfYyhkP1D",
	"7r17Wkk5DezZCDsVqLFqLcbU2brer2KMiCebT1J4SjXBAeMfPGy",
	"7rVHNyG5byhpG1ZGwApfBx76WdBFtJtQqnTVn4pAPK82cdqVwGP",
	"7rPtUL7LRGXp3yJRffw45qCuUdmBQhZpvPzajNNU6dhUr2KnWGZ",
	"7qzwLEVYSwrm5QJuLXTMpLjprRxCXD3PLV1DECF8TKNgvkhsc5w",
	"7qkX3itCCffSPPHr5TWgzAfuz5u1N5aB1h98xrRX2hoiyyeBGW8",
	"7sC6CQLVwjQV4WUUh7n2sgBJhkBG3vVjyuXdJKXzQgZBsUpB2qa",
	"7raEvvopTGpJyZsSUzqjsbgwR9HWHwQwZ3aVDTvqAHPgQbyNXQC",
	"7rEiVo6x7VEkvj2aMngqNiKU8srrJK2vhHSKQ7Tkes9NaYMtXvv",
	"7rFk6dDG4zJhfC4fTApq1baB8Wp76WCpusopMbG9LJhGKB9LQqu",
	"7sAmt1WdWVVobUcv1B8Tzmxg64vimJ54RPSao5MPyjehtxEkL55",
	"7sJB67hdrWzVYLWMZLm9Xc45Qu336f6UUBm2rUNxmpjVpaHTQTU",
	"7s6LLj8cMz59qg4fJrCoNfCspRhknMYxGhuTNj9bEFsEou7bkqb",
	"7qyfSWLcySfmqXHuCHDGXagJoWdntQVYkJnCe8XikMBaPBm4p7H",
	"7rjUu26dohqNAcNmXUyP8VX5MeVfrYwBkwtgyMGGEbsDTZXuWJb",
	"7rHxa7qTgkSNNE1T8BKEWMH8EugdkKgcGYg1k4q1XEi8bSgWjBp",
	"7r7bei3PPYhS6qubxavHZ8tG5tRNNP3VBNGPSJax7HRZMUh8THL",
	"7r7RER7iRvkgqMvLwG3a4PM7vEC8okkvoQoEnbYkF6zYe4Bwi7x",
	"7qknM5XnibTkoHtjPz2sVELs5CDAGd5osTqgXkUgvACYz7w58jU",
	"7sKUyPiiqjpVDvxTLETCtaWTJ2KwWBjrzSSp9TXPfD8g4CCdv2e",
	"7sSPAWJUzmUs9fMqGbdRkRnv8TtaHYZtzr1HA4XnXVn46dqdzdY",
	"7rhC4MF325WZtZFQdfMGWx7i9egjYkw9NWErdZ3SqfMZkLdfFQS",
	"7r9de1Gi1TYA2ipFQALsp7fu56MBpDrcA4kDkPtZNAjfKvzNLPN",
	"7sUtfGXm3t2wd89t2duSgJGw24HcRZTWViARFFFzLz3YeC143rs",
	"7raQKi3CDRy9wm1hgQFYon4u8ihWNAjwCHRed6TEjbQT2aVUSUd",
	"7qxhSPBDSLLJcJ3X5kKcZMxPqX6JqGwEXCXSF5ZxrpP4moFAWRw",
	"7sV9u7s9a16XdusfGkLMu9oD6NoEWzwvmiDwHxEctbNgvjQucAL",
	"7qxbr6CSXdwYDELLdfuzSdRPNipkdRBLg1VBAFjup8kYNte8T86",
	"7rUxfN6ebTq2o1LmprD3EshjyHRYJX6ssV3FSCJ5QsymUd2JqLC",
	"7r54GFtEYorNbYYvihUTnv9uehzbk8CWHzF9HTj3nvE2fziH5B6",
	"7rXG6aFxQkqxdWuSjQNScc9YCfCTG596VrFSKKrgscoHWLrHC1Y",
	"7sNKzuwG46utT3TbJK1gqurvTUoss9ipZHKwVpHHq6h8R3QqoCt",
	"7r1fUYP3w6RAriZE3Nahe9aut4JHCTJWT1tNpAerFuDb4YMwGDg",
	"7qoQQ2dr1fZ9UmVCzB8GQWeQcpFsEDMjai2R3d6mH2xQ3xKDMDt",
	"7rDeGBqtDEnoJcXngkPfqEu4JPLTtPGS6FT1Eji1HDFyzgHWKZs",
	"7s4S7Zy9RB1pnXGC7WzVHW8e1f47c1kJV78P8mnQtRX47z3CY1S",
	"7rPPkZa9qdwrHii9ynZLDGPU4uJdhaKREBk5eCYe1E7fKh2PTtm",
	"7rkxyDkfi6g27ZTq7hkQCJJgMB9CRHqGaQivdMsJkxCvFvVqyeg",
	"7s5WV3N7uctgtrHHJphcCwsavqgbehzrUwtx7TE44VouJXrwVTa",
	"7quB9UtwntxVnerUxjt4FtUceSmosRdYtwJoDCzXYnkFNpmdha1",
	"7s4aor6Jqo35Qpu9zi79htvuwmT1XqHNv7K98Y9ZJQonvomVFyA",
	"7rQXsvBMxj27YJYKrv38uCnTQXoKzNnt2Hm38n3zRjCDqssx556",
	"7qjyeJoK4TuHyCvsrXMv2Y24hcjvnYrcF9zQs33TZHgcDAvpm2i",
	"7s3HPyDisa7LiKgoyzT6fbEmLhWSV8xtZtSmkvsMQr9Lmukxqbw",
	"7rDSkn6ky7ciZvtfYXKJRtSacAp1w7WXmCCinAeqtpP6t13FgGx",
	"7rdXiD4wM5oxEMZ7QtyuR75PLehizF8VQpStM81wLQTy5fzF7ah",
	"7rM1VmRnZsd9iNC34NjH3M96y5RAWPnUSQNz9WenPiDHRzmDRQJ",
	"7rBGyrJXcUzL7bm3RGoEEfCQBU9SRgur2RAA5CTwfGs2W2ciRA9",
	"7qhzB85z7XE1Xqfv8nSNTdorsSwppq2cuMmYEVTtpW4f9UkAoZq",
	"7sP4TkrZ2VXAFe7o96HCrKT8W8NbfRNnbiUY3NQVFL1ReQYt6Uy",
	"7qpkDGgsV2QoUkb3g1P6KKgLLdxfyrt6CpyPz2YSjcupnFHNY38",
	"7rayyysNAPauT8FxhN3KM79W294Y5HZ2vVWt91TnHzPzQ2aHkDu",
	"7raiG6eJayNsgeMZcUcQe4LXWyFPcQqYbG66zbvPwZie2qcTRML",
	"7r3z6Wf4S6LJJvW5RwjdNfsD6mWjPTAKKSwfLYHAw7H74s1vuMs",
	"7sQz9nvesVbqdYnG5KBhP8pPdNxbm4Sw9AYJrxwwwhc6vszAYeL",
	"7ruDkeu52JjL7haLJVW1hXAhArrdXbUhiAeMGpUEdNMQ8bUsTaZ",
	"7rTUk7Wgzc478EBx5EGouhBLspLSwftH3Cs6osDfYx3UGZMyooj",
	"7rwENKqdvvc7KWeoyfJHi27xuWutgbUPuUzLWKXRdi52qGs7sAz",
	"7rR9NDX4iM2QuCbx9jQW7yrrH7hrE6buCs9iuEYEt5Bg1v5sY4z",
	"7sJcCue2Fo7H68oFFVviiNvG8LWvAwahZtJrEr4n8sZtULFwogs",
	"7sR7wRqo19tmz2SfPkDYSmVFBNabjHeUy9xbAviRhQbGjE7tdbB",
	"7rg83zevgKj9EqayjUgVz7k8gegNwCfWvohHf351V6yJiJF24CF",
	"7rrDf7tP5KNVSw5t9BosSd4YCzr8YdBvxRjzdUCoGWYxsZkrUmW",
	"7rjFeZB5ekCt48UUMWUoyWQJbhnqHsjZTGZSW43g6UBRVDBshTd",
	"7sMS2qX6vHySkRGeDDibuYxSuoQ2jYJUT5oRNJsBQkEXKmxeJGf",
	"7rjAKhQZQwhAss93XsNtsrugaSWby2t1F55yD32VNJzWC5iUqRY",
	"7qpy8jcWmW7h2gC3mGxbQ1d1oUwHhry7uAmuSQZwPsBbQnc29ij",
	"7r8pYR8baPw2Em46Z6YxuwhCsjMYfd5HpUi2uuH266XVXJX2VTt",
	"7sBrYkS4AYts7ENoy7HKHd6KJnQL9vYpzPqxcQdb1mG64PjivFx",
	"7r3xp71YgSJdqvAdvyDRyegAzuZEFDFPtYoDi93bueV7g92fpEM",
	"7rJSRaBLia6QtwX9v64T2CHtZu41k4FoeGeWMfsKsN6E8keX2Ds",
	"7r8v3iRYRKP3h6KUVEGbKJPCJ3EjCwDaTSFFDPzurSNmkk4K935",
	"7sR16rSFWzps1wW5RxFzcGdcpJkbK2GBnt43mjaBeHTPq84gnGV",
	"7rMXCtvCdWDXPj4B9x7dfXyVyzJPD4AXZxoWFgEHKP8N7piu6w3",
	"7qagJQa4nRhc4qqxe8Uig5bNYrrEMUyHcVoxGUcB8no68GMfFRy",
	"7qqTjYqaNWC6pqdHDeCGcxC6kvpKEcct7ijFx9ktVY6vkVzZRih",

]

new_data = [
	"7qjE5Z9SJJk9ZzPoYnfzDKn1mVz4TKXniUbws7AeMmesFfiyk2w",
	"7rYGX6FtRoTwpwh6CEm7Lvgu1kVXQHTucsW7JkGJSEXjKkM1LCz",
	"7rkGrN3rhnea53vf9uyXQR41mQo5myrhRC8V9wRKiU5CdFMJMp5",
	"7sAz391E2ygaHWsmU8ScbZN1QHj2MQ67eLD9UKhzDw4SqQybMXE",
	"7rAptqGpbzeaABCEafkvC4irFVZ3Ayf52WLnnfnYgHRiXNEDGmN",
	"7riWdLxx7WK9w8FfUAx9cXzw1du53ZJopSwfzfVaHaXvcG9E9DT",
	"7qaCbh2BBC5HavWJz5JYDSiWcuMnEvVRd2viHSgE61FZQpDt3m2",
	"7rjyAPFDgADmM9xjNmMrCtiEDqQieRwzJ4DCXiW9PrBAjuPArTT",
	"7rqNSgkwRZaHvNp4LRb3aRfThXSoW8JkmKA9ppXNExCV5BUsnFJ",
	"7s2w1nyQarP9xg1wAzFHR4uBRGRTtWB6kifrRzufm2BsBuCyuzq",
	"7rZec8mEWZX4fmkfC98qbo47mufRRETkELG9tdrq1DnkVCSSjbo",
	"7rpMsXYLutrPGMunuJhJFeiqKB3aqBApeXNi3xmizqpqru6r5vk",
	"7rv7XwgdoLTPpKXeiogpAGA9yYMyhUPWnDBrrmTDjkvP8E4e7Wy",
	"7s7X4nJhM8nz5n8eS4fp25nKmWJLUQw4QBpb7uVPbiX5Rbr5AYD",
	"7rogQahrFXe5opdVDfVzYwhy2DYK1F3aSRHiUGEojBqbiW8naUC",
	"7r5FnaW5AhSB3GVugM7cvyXkekyFo5xCrtiFi4KS2DB9azv3y75",
	"7sFk11Afs1goqXKpTTcmtXGHejbWsNbU9YmhAYSXX9Y1HfDVreV",
	"7qcT34Edp5XwtEk5r2RUgktAMmB8zfAY1KK5NMu7fXsQF2v6XA3",
	"7rCnRAXSUyYNukVifwuWMWfFddECWRqqKE6FeTquNDfL71hYZJG",
	"7sM19uTwM9igLELgrJo3B5kF21fcdC45czk1FThTi5WDMrfDEun",
	"7sCZUacrnuAEvRkav1v97YfvJRyQKv9iyKVCfy1E4mVTwfffv7L",
	"7rhHFP2ngS7WbEVBCdyU9eiudyfe7n67ccYzNRertYR3mbWvjkf",
	"7rvKL2RPETYjmCnMDaE2FnAsZcBew5UQA1c8aVdQD8F73TddjJ6",
	"7rh5CnmEXe6WM6fwvSnyBfXQQTWPM9csvnZogWtUxFpbpAriumF",
	"7rbH1sG7vw1JndvSSXCj9KAWVwTX3318nkdD6838bMf2bCMHMp5",
	"7sBRBvsy66V9DycqpNoJYXyoRBCYNRWZEqZHpMiVNhVfL2wQaL6",
	"7r7KSeHWTUrnwZNA8hHxxXFmuchqxyfjjbE2aFdUvDUg2Z4QcxJ",
	"7rexz9EWM4mwnjMCgZCBvYh7qeVzWNCW2WSThkrQACk5XPU8duN",
	"7reQgz41Jdt2FzAH7ksSwLi3JfoUu3d3cBGXsTvCZkNJuyE8SqR",
	"7r93Qyu62NrZV6BYSFCbzQLDpxG5XWxZQ42ZmtVeq4wFe62pkbi",
	"7sNJhYGdzXjsGSGBn9z6yghRoUbWj6rzV7Re8xqp5Xzm1wTcix9",
	"7rCgC3YMfzp3tmtSaeNUoSfQ5P6VhP9JnhTry29WcqswjHj5PXK",
]



for x in new_data:
	if not x in old_data:
		print(x)
