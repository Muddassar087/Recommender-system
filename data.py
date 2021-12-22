import os

directory_path = os.path.dirname(__file__)
file_path = os.path.join(directory_path, 'sources/product images')
starfilled = f"{file_path}/star-filled.jpg"

products = [{"product_id":321732944,"name":"Rado watch","cetagory":"watch","img":f"{file_path}/Rado watch.jpg","average_rating":5},
{"product_id":439886341,"name":"chrono watch","cetagory":"watch","img":f"{file_path}/chrono watch.jpg","average_rating":2},
{"product_id":511189877,"name":"gold watch","cetagory":"watch","img":f"{file_path}/gold watch.jpg","average_rating":5},
{"product_id":528881469,"name":"leather belt watch","cetagory":"watch","img":f"{file_path}/leather belt wacth.jpg","average_rating":3},
{"product_id":558835155,"name":"Louis Vuitton handbag","cetagory":"bag","img":f"{file_path}/Louis Vuitton handbag.jpg","average_rating":3},
{"product_id":594012015,"name":"Sunscreen lotion","cetagory":"lotion","img":f"{file_path}/Sunscreen lotion.jpg","average_rating":2},
{"product_id":594017343,"name":"tropical lotion","cetagory":"lotion","img":f"{file_path}/tropical lotion.jpg","average_rating":1},
{"product_id":594017580,"name":"shopping bag","cetagory":"bag","img":f"{file_path}/shopping bag.jpg","average_rating":3},
{"product_id":594033896,"name":"Iphone X mobile","cetagory":"mobile","img":f"{file_path}/iphone x mobile.jpg","average_rating":4},
{"product_id":594033926,"name":"ipad","cetagory":"mobile","img":f"{file_path}/ipad.jpg","average_rating":5},
{"product_id":594033934,"name":"samsung mobile","cetagory":"mobile","img":f"{file_path}/samsung mobile.jpeg","average_rating":5},
{"product_id":594202442,"name":"realme C2","cetagory":"mobile","img":f"{file_path}/realme C2.jpg","average_rating":4},
{"product_id":594287995,"name":"fragrance-women","cetagory":"perfume","img":f"{file_path}/fragrance-women.jpg","average_rating":5},
{"product_id":594296420,"name":"daisy perfume","cetagory":"perfume","img":f"{file_path}/daisy perfume.jpg","average_rating":5},
{"product_id":594450209,"name":"marc-jacobs-perfect","cetagory":"perfume","img":f"{file_path}/marc-jacobs-perfect.jpg","average_rating":5},
{"product_id":594450705,"name":"tofrod perfume","cetagory":"perfume","img":f"{file_path}/tofrod perfume.jpg","average_rating":5},
{"product_id":594451647,"name":"mouse-keyboard","cetagory":"electronics","img":f"{file_path}/mouse-keyboard.jpg","average_rating":4},
{"product_id":594477670,"name":"speaker system","cetagory":"electronics","img":f"{file_path}/speaker system.jpg","average_rating":5},
{"product_id":594478162,"name":"olive oil 1","cetagory":"lubricants","img":f"{file_path}/olive oil 1.jpg","average_rating":4},
{"product_id":594481813,"name":"T-shirt","cetagory":"cloth","img":f"{file_path}/T-shirt.jpg","average_rating":4},
{"product_id":594481902,"name":"Navy blue T shirt","cetagory":"cloth","img":f"{file_path}/Navy-blue T shirt.jpg","average_rating":4},
{"product_id":594482127,"name":"local shirt","cetagory":"cloth","img":f"{file_path}/local shirt.jpg","average_rating":4},
{"product_id":594511488,"name":"Girls T shirt","cetagory":"cloth","img":f"{file_path}/Girls T shirt.jpg","average_rating":5},
{"product_id":594514681,"name":"Koren T shirt","cetagory":"cloth","img":f"{file_path}/Koren T shirt.jpeg","average_rating":5},
{"product_id":594514789,"name":"Dell XPS 15 laptop","cetagory":"laptop","img":f"{file_path}/Dell XPS 15 laptop.jpg","average_rating":5},
{"product_id":594549507,"name":"hp pavilion gaming","cetagory":"laptop","img":f"{file_path}/hp pavilion gaming.jpg","average_rating":4},
{"product_id":594549558,"name":"battery 1","cetagory":"electronics","img":f"{file_path}/battery 1.jpg","average_rating":5},
{"product_id":743610431,"name":"dell precision battery","cetagory":"electronics","img":f"{file_path}/dell precision battery.jpg","average_rating":4},
{"product_id":777700018,"name":"mac book pro","cetagory":"laptop","img":f"{file_path}/mac book pro.jpg","average_rating":5},
{"product_id":840017677,"name":"jeans","cetagory":"cloth","img":f"{file_path}/jeans.jpg","average_rating":4}]

prodDisplay = [products[0:6], products[7:13], products[14:20], products[21:27], products[28:30]]
