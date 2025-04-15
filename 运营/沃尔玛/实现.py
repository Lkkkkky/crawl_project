'''
=========================================================    
       @File     : 实现.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/4/1 18:10
       @Desc     : 
=========================================================   
'''
import requests



for i in range(200):
    headers = {
        "accept": "application/json",
        "accept-language": "en-US",
        "baggage": "trafficType=customer,deviceType=desktop,renderScope=CSR,webRequestSource=Browser,pageName=searchResults,isomorphicSessionId=NI_3EqXIdRa0GMPn54Jaa,renderViewId=0d7f86e0-4fe5-4c07-84fb-f9729f4596d7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "downlink": "10",
        "dpr": "1",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.walmart.com/search?q=phone",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "tenant-id": "elh9ie",
        "traceparent": "00-183229e4a4fe685b5c062a06e61026b9-0612f1043203699a-00",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "wm_mp": "true",
        "wm_page_url": "https://www.walmart.com/search?q=phone",
        "wm_qos.correlation_id": "zw8Qg8G5fPsq-yxQ9PwjVe_-c5wyPUqFBclh",
        "x-apollo-operation-name": "Search",
        "x-enable-server-timing": "1",
        "x-latency-trace": "1",
        "x-o-bu": "WALMART-US",
        "x-o-ccm": "server",
        "x-o-correlation-id": "zw8Qg8G5fPsq-yxQ9PwjVe_-c5wyPUqFBclh",
        "x-o-gql-query": "query Search",
        "x-o-mart": "B2C",
        "x-o-platform": "rweb",
        "x-o-platform-version": "usweb-1.191.0-69299c417d3bfeab12899d8c7dd48bdee00220e2-3271729r",
        "x-o-segment": "oaoh"
    }
    cookies = {
        "ak_bmsc": "4830EE2D556AFF2C1D52DFA98CEA5C5B~000000000000000000000000000000~YAAQpnw2F8BzOa6VAQAAT0zR8BtiowyCsaEiYvwFBmE+R+Q82rrt1KfoM1s5c7fi5iHbnPNSrRaIOGTohDUYc3ITjA8bw8E2l0g+GtoAkMKEtK0Vayy2nz7CBP3+rNFwStrlZa1SlTKFbClGXcCt8UYk9Oo+4emvtganBxVnYTaHov7axhpM0zaj1sTxbrwx8sTpmr6knVkEenUjew7ThU5YmeJMeXoB+oc5QpZdHKcYn5L6urKCda8ToRfJScukFnIlC0ttTO/Xo57ePQCz5ripx+JfFWevGJ23i1SL4fHdbKnvzHqFRFNSTh9DejnVdc+pWRN/rQJIpycAdzf/C8AVln3IjrwcYIhFe/cRW+YjeSXjZ91wvldigYLPjSPfEAZNLlTVpLeObWY=",
        "ACID": "ef9970a8-6933-461d-a94d-cf7ddc2f049e",
        "_m": "9",
        "auth": "MTAyOTYyMDE4rv7J6aIFIgOzDruy2VQ%2FMpcisGrLMKpDnfaTfNQ0KPl7%2FWZFazgHQglMNVMWPoKnH7VskmrYEzaGn5qOS07XUEk3ij6caxpcVZThVH9Rwn%2Bv%2FiO0YUhhBMkmTVfdRR%2F9767wuZloTfhm7Wk2KcjygglTqinKgSpV0hco0QKmh1DdW1eFNuKpIj7aTJYUWlXHpB5f6SZS%2Fv4bmoJ%2B%2BBQnuL6c9d1O%2BI5zzFLxumhM6lkUMk70P8glgOEpLOprhDfMWpzMbgzyqWg6MoSOREDGWmXwdwx4e1RUeIS97Etr9u9tNjLN6rQqOTbOLS9BCD%2BMR4Sau6%2FslI%2F7WT185IP1VK0MQQmqMGL1FX%2BOR7d63QP8VJf2OLLdJo5D1q5Xn8X4Esohd7R4evQPcvSpE%2Fn5DpE5WBBdZBCyKnCQAR7o6eg%3D",
        "hasACID": "true",
        "abqme": "true",
        "mobileweb": "0",
        "xpth": "x-o-mart%2BB2C~x-o-mverified%2Bfalse",
        "xpa": "-jnZ9|0vWkn|3VCVY|4huUt|AcM0s|AqF11|CElIJ|DF_fw|DWA1K|Hgu7J|I-Dl8|KhOVs|LRSst|OQe8n|QNY8m|Qf8pP|TO4NT|bLuFh|c2jMw|cYOXT|dWYMK|fdm-7|gZWrW|h60LK|i3eO7|jM1ax|kbHab|l-yEM|pXvSG|pn0ka|xf36q|yAoIi",
        "exp-ck": "-jnZ914huUt1DF_fw2DWA1K1Hgu7J1I-Dl83KhOVs1OQe8n2Qf8pP1TO4NT1bLuFh1c2jMw3cYOXT2fdm-71gZWrW1h60LK1kbHab1l-yEM1pXvSG1pn0ka1xf36q2yAoIi5",
        "_pxhd": "642ac6a2f61578102f49e77d1336b42acd7c8c59b71655a533dfdf5696db20af:0488c2c9-0ee1-11f0-b005-6814dd1c9bb6",
        "adblocked": "false",
        "vtc": "fg0QwxRYGyND7FfUVp6k7g",
        "bstc": "fg0QwxRYGyND7FfUVp6k7g",
        "pxcts": "05849b8f-0ee1-11f0-9102-9e6dd6064e7a",
        "_pxvid": "0584904f-0ee1-11f0-9102-5ededf7990d3",
        "io_id": "a1b8e8d8-335b-4385-9b22-588b261a6016",
        "if_id": "FMEZARSFlY+QEOt/hY0430eZpX8MkeS2qimdeOq/Ya6b6KZAZKPWxJHuUKHScDTzbU3nr/rOc5yUjF9CNExN+BlHvD8mGFBwgQb+V2ZnhPpObfqto7WBg+RVgFaZYa7eZGnBOExo6NiclFHKoncG7T07/GsmAZPuqi7CGTKRqWMuy/ukwWq+2QpDpy4Y6H2sLqJsoIOvyscdlukpHexvuAgdZ2D+I+USE2akubQ5jcvwe4Z+t3jiiaVo0pTRYbre2Cx6adLyvfLpWIGyE/ANjpmtGM3UELmKK7VbAVdUa8pbWF6XdhUua0CHnTupDr+EWbuigbMTHCHDFFoO2KPt3g==",
        "TS016ef4c8": "018bbeb01a6055d8711c9cbd450052f746bedf9fe65f83c1ad8fd953e4d501c5d1e58a3f111004f52e31e63f86c99294736f5e6cf9",
        "TS01f89308": "018bbeb01a6055d8711c9cbd450052f746bedf9fe65f83c1ad8fd953e4d501c5d1e58a3f111004f52e31e63f86c99294736f5e6cf9",
        "TS8cb5a80e027": "0880589ea5ab2000256163b692af6bb6cf08c6b66648806eae4c8c01941de38953a229941faf609c08734b942f11300006037b8279e1c0b0d718de33af97396d3cfe187eaf5c753bd0836ec5d0c71b8ed78d13bf447407ff82cc79c2a60c36ae",
        "xpm": "7%2B1743502006%2BRqxRL-mdoLPveBMMKS6Lxs~%2B0",
        "bm_mi": "54FA1E2AA936A826517F49C17EFAD024~YAAQpnw2FzGROa6VAQAAeSvS8BtgS0DmwhQvUebAYwYxQ0czZn4oLL6Yv7IzCQcuY5dVJgebS4iR6c8t4ICccMJ6w883cSFBGfWkdroYHfwcI04Nf8ILGi5UtheOiePPa+ppZX9zZ8v83aG5D90hEUSK1qrvHUfyPhGZIdhUm4X4t19un1Ud8cqORK/d9OI8a92hmPxH1dO1hHAKflPkHR6yRIcQb3wZSuQBndpQ8Vsw9VFjFb8kzMkkOG5DzmjH5TLLxJJJtoPLZk5hHgzmd0WHUx8jZijerQVd8muD+xKqTgLGB0a3rVFrle13kL4=~1",
        "_astc": "5130b97f9acd9bd35917e8781e6d686f",
        "_intlbu": "false",
        "_shcc": "US",
        "assortmentStoreId": "3081",
        "hasLocData": "1",
        "locDataV3": "eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJub2RlSWQiOiIzMDgxIiwiZGlzcGxheU5hbWUiOiJTYWNyYW1lbnRvIFN1cGVyY2VudGVyIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdFUkJFUiBST0FEIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJhbGxvd2VkV0lDQWdlbmNpZXMiOlsiQ0EiXSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX1NQRUNJQUxfRVZFTlQiLCJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdLCJ0aW1lWm9uZSI6IkFtZXJpY2EvTG9zX0FuZ2VsZXMiLCJzdG9yZUJyYW5kRm9ybWF0IjoiV2FsbWFydCBTdXBlcmNlbnRlciIsInNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQifV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6MzguNDgyNjc3LCJsb25naXR1ZGUiOi0xMjEuMzY5MDI2LCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTIiwibG9jYXRpb25BY2N1cmFjeSI6ImxvdyIsImdpZnRBZGRyZXNzIjpmYWxzZSwiYWxsb3dlZFdJQ0FnZW5jaWVzIjpbIkNBIl19LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTgyOSIsImFkZHJlc3NMaW5lMSI6Ijg5MTUgR0VSQkVSIFJPQUQiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNn0sInNjaGVkdWxlZEVuYWJsZWQiOmZhbHNlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOmZhbHNlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJpc0V4cHJlc3NEZWxpdmVyeU9ubHkiOmZhbHNlLCJhbGxvd2VkV0lDQWdlbmNpZXMiOlsiQ0EiXSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdLCJ0aW1lWm9uZSI6IkFtZXJpY2EvTG9zX0FuZ2VsZXMiLCJzdG9yZUJyYW5kRm9ybWF0IjoiV2FsbWFydCBTdXBlcmNlbnRlciIsInNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQifSwiaXNnZW9JbnRsVXNlciI6ZmFsc2UsIm1wRGVsU3RvcmVDb3VudCI6MCwicmVmcmVzaEF0IjoxNzQzNTIzNjYyNDE3LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6ZWY5OTcwYTgtNjkzMy00NjFkLWE5NGQtY2Y3ZGRjMmYwNDllIn0%3D",
        "locGuestData": "eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTc0MzUwMjA2MjQxNCwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCJ9LCJzaGlwcGluZ0FkZHJlc3MiOnsidGltZXN0YW1wIjoxNzQzNTAyMDYyNDE0LCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6Ijk1ODI5IiwiZGVsaXZlcnlTdG9yZUxpc3QiOlt7Im5vZGVJZCI6IjMwODEiLCJ0eXBlIjoiREVMSVZFUlkiLCJ0aW1lc3RhbXAiOjE3NDM1MDIwNjI0MDgsImRlbGl2ZXJ5VGllciI6bnVsbCwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCIsInNlbGVjdGlvblNvdXJjZSI6bnVsbH1dLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EifSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE3NDM1MDIwNjI0MTQsImJhc2UiOiI5NTgyOSJ9LCJtcCI6W10sIm1zcCI6eyJub2RlSWRzIjpbXSwidGltZXN0YW1wIjpudWxsfSwibXBEZWxTdG9yZUNvdW50IjowLCJzaG93TG9jYWxFeHBlcmllbmNlIjpmYWxzZSwic2hvd0xNUEVudHJ5UG9pbnQiOmZhbHNlLCJtcFVuaXF1ZVNlbGxlckNvdW50IjowLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6ZWY5OTcwYTgtNjkzMy00NjFkLWE5NGQtY2Y3ZGRjMmYwNDllIn0%3D",
        "akavpau_p2": "1743502664~id=e9c40c5a395170eac07795e6ba031f60",
        "xptwg": "3121001305:1D1A3BF916EE520:47B102D:1B70838D:6B51A484:C537BA06:",
        "_px3": "61a2c87b5ac0b1836579fb6b25c92aabc2cdb7d31e48fc3014a6416f92a53c15:pgZWNFsReo/uKgPcbMaDclghhpBeBn39f94R4ptOAF3TkKS3uTzAl7NRwG0dvJ4LaXy49uwfiSaS9by1d1ED+w==:1000:WOBudmNnGCr5UvFjrcLf1g8z+CvUf7t+uhfNA9ymlbCkrq94HhJVnfgTAk1JqKxQaE894JJNubg9EUYar9szjdONdXoCfNyHKxaI8GFIqtMhmtW1r4lmyYFudDAQqXd3SxlmPMB/79ddIGhLdx1TG3fV9mCPKGSpOGnaKO0kl81FEZ+rWX5j12jHIzRULXuG389f6BVmNZljS9aAi87DplFFE9PmATvMfVQLCgLp5WY=",
        "_pxde": "3272e93b9487a26f1693c291a3e851afd0afd1fcf6e1107639ab01b95e8dacaf:eyJ0aW1lc3RhbXAiOjE3NDM1MDIwNjQyODV9",
        "xptc": "assortmentStoreId%2B3081~_m%2B9",
        "TS012768cf": "01d032572adb74ec7183a6bee198e1240fb3e3c6a09225bc080a9757cac52230c23f1ff935a8316066b2551b47b3624eff201d0324",
        "TS01a90220": "01d032572adb74ec7183a6bee198e1240fb3e3c6a09225bc080a9757cac52230c23f1ff935a8316066b2551b47b3624eff201d0324",
        "TS2a5e0c5c027": "08edc6f644ab200049146230e1e95d208194e7da03bbf7afbc1d25e9d17df010e662f02a7bd1185608ef11da5e113000addd23613afe3cf746ab1eca07702d440a40e85cc4764a2cf4154572f7e8fb3eb85381a7cd7e1af7483ed6ae04ebaff1",
        "bm_sv": "75A6042D919B2347EF8CBB917E07FB6C~YAAQpnw2F96TOa6VAQAA+T/S8Bs5hS9SZAprLMIt/LTWCGPJiQMtodgN8d5JhypFHkgRuTOZncAEt2j54t/IEyARSjM95rRTRuKMvKaSTG78lImEDUtOtb10oCZ8Nm71pCWGj27/utba7qk/o1H/wxSK17cFLju9WfXqTBtngnqNouqnUFG6TxfRth7tZLql/c2uTHKi8CQTEzRGQUXrFoYndswyBbVWkdoJuhOp3IIEU5LLNuhCj8VOdquWrMYOMA==~1"
    }
    url = "https://www.walmart.com/orchestra/snb/graphql/Search/47da39fb71b622d0ce183626bff47dff8a76149b8d949f3b7de62532aeff76e0/search"
    params = {
        "variables": "{\"id\":\"\",\"dealsId\":\"\",\"query\":\"boy\",\"nudgeContext\":\"\",\"page\":1,\"prg\":\"desktop\",\"catId\":\"\",\"facet\":\"\",\"sort\":\"best_match\",\"rawFacet\":\"\",\"seoPath\":\"\",\"ps\":40,\"limit\":40,\"ptss\":\"\",\"trsp\":\"\",\"beShelfId\":\"\",\"recall_set\":\"\",\"module_search\":\"\",\"min_price\":\"\",\"max_price\":\"\",\"storeSlotBooked\":\"\",\"additionalQueryParams\":{\"hidden_facet\":null,\"translation\":null,\"isMoreOptionsTileEnabled\":true,\"isGenAiEnabled\":true,\"rootDimension\":\"\",\"altQuery\":\"\",\"selectedFilter\":\"\"},\"searchArgs\":{\"query\":\"phone\",\"cat_id\":\"\",\"prg\":\"desktop\",\"facet\":\"\"},\"ffAwareSearchOptOut\":false,\"fitmentFieldParams\":{\"powerSportEnabled\":true,\"dynamicFitmentEnabled\":true,\"extendedAttributesEnabled\":true,\"fuelTypeEnabled\":false},\"fitmentSearchParams\":{\"id\":\"\",\"dealsId\":\"\",\"query\":\"phone\",\"nudgeContext\":\"\",\"page\":1,\"prg\":\"desktop\",\"catId\":\"\",\"facet\":\"\",\"sort\":\"best_match\",\"rawFacet\":\"\",\"seoPath\":\"\",\"ps\":40,\"limit\":40,\"ptss\":\"\",\"trsp\":\"\",\"beShelfId\":\"\",\"recall_set\":\"\",\"module_search\":\"\",\"min_price\":\"\",\"max_price\":\"\",\"storeSlotBooked\":\"\",\"additionalQueryParams\":{\"hidden_facet\":null,\"translation\":null,\"isMoreOptionsTileEnabled\":true,\"isGenAiEnabled\":true,\"rootDimension\":\"\",\"altQuery\":\"\",\"selectedFilter\":\"\"},\"searchArgs\":{\"query\":\"phone\",\"cat_id\":\"\",\"prg\":\"desktop\",\"facet\":\"\"},\"ffAwareSearchOptOut\":false,\"cat_id\":\"\",\"_be_shelf_id\":\"\"},\"enableFashionTopNav\":false,\"enableRelatedSearches\":true,\"enablePortableFacets\":true,\"enableFacetCount\":true,\"fetchMarquee\":true,\"fetchSkyline\":true,\"fetchGallery\":false,\"fetchSbaTop\":true,\"fetchSBAV1\":false,\"enableAdsPromoData\":false,\"fetchDac\":false,\"tenant\":\"WM_GLASS\",\"enableMultiSave\":false,\"enableInStoreShelfMessage\":false,\"enableSellerType\":false,\"enableAdditionalSearchDepartmentAnalytics\":false,\"enableFulfillmentTagsEnhacements\":false,\"enableRxDrugScheduleModal\":false,\"enablePromoData\":true,\"enableSignInToSeePrice\":false,\"enablePromotionMessages\":false,\"enableItemLimits\":false,\"enableCanAddToList\":false,\"enableIsFreeWarranty\":false,\"enableShopSimilarBottomSheet\":false,\"pageType\":\"SearchPage\"}"
    }
    response = requests.get(url, headers=headers, params=params,
                            proxies={'http': '127.0.0.1:33210', 'https': '127.0.0.1:33210'})

    # print(response.text)
    print(response)