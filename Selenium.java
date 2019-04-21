//# xpath & Css Selectors ==========================================
	[@attribute='value']
	[@attribute='value']/following-sibling::element // travers to next element
	element[@attribute='value']
	*[@attribute='value'] // select all
	element[text()='value'] // reach by text in element

	[attribute='value'] //cssSelector
//=================================================================//



//# Setting Selenium Path in the project============================
	System.setProperty("webdriver.chrome.driver", "path");
	WebDriver driver = new ChromeDriver(); 
//=================================================================//



//# Handling HTTPS Certifications===================================
//  https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities
	DesiredCapabilities capability = DesiredCapabilities.chrome();
	capability.acceptInsecureCerts();
	ChromeOptions options = new ChromeOptions();
	options.merge(capability);
	WebDriver driver = new ChromeDriver(options);

	capability.setCapability(capabilityType.$,true); // configure custome settings
//=================================================================//



//# Handling Alerts ================================================
	Alert alert =driver.switchTo().alert();
	alert.accept(); // or dismiss()
	alert.getText();
	alert.sendKeys("");
//=================================================================//



//# Handling Elements ==============================================
	WebElement element = driver.findElement(By.id("id"));
	//or By.class("") | By.xpath("") | By.cssSelector("")
	//element can be used instead of driver (ex. footer.findE..)

	String key = Keys.ENTER;
	String chord = Keys.chord(key1,key2);
	element.sendKeys(key); // or chord
	element.clear();
	element.isSelected();
	element.isEnabled();

	List<WebElement> elements = driver.findElements(By.class("class")); 
	elements.size();
	elements.get(i).click();
	elements.get(i).getAttribute("attribute");
	elements.get(i).getAttribute("").contains("");//T-F
//=================================================================//



//# Handling dropdowns element mostly <select> ======================
	Select select = new Select(element);
	select.selectByValue("value");
	select.selectByIndex(3);
	select.selectByVisibleText("text");
//=================================================================//



//# Assertions : stops the script if False =========================
	Assert.assertTrue(element.isSelected());
	Assert.assertEquals(element,vlaue);
//=================================================================//



//# Handling Syncronizations ==============================
	WebDriverWait explicit = new WebDriverWait(driver,9);
	explicit.until(ExpectedConditions.visibilityOfElementLocated(By.id("")));

	driver.manage().timeouts().implicitlyWait(3,TimeUnit.SECONDS); //implicit
	Thread.sleep(3000L);

	Wait wait = new FluentWait(driver) //fluent
	.withTimeout(10, SECONDS)
	.pollingEvery(2, SECONDS)
	.ignoring(Exception.class);
	 
	WebElement element=wait.until(new Function<WebDriver, WebElement>() {
	public WebElement apply(WebDriver driver) {
	return driver.findElement(By.id(""));
	}
	});
//=================================================================//



//# Performing Actions and AJAX Calls ==============================
	Actions action = new Actions(driver);
	action.moveToElement(element).build().perform();
	action.dragAndDrop(source,target).build().perform();
//=================================================================//



//# Switching between opened windows ===============================
	Set<String> ids =driver.getWindowHandles();
	Iterator<String> it = ids.iterator();
	driver.switchTo().window(it.next());
	it.hasNext(); //T-F
//=================================================================//



//# Handling Frames =================================================
	driver.switchTo().frame(element); // or .frame(i)
	driver.switchTo().defaultContent(); // once finished with frame
//=================================================================//


	driver.manage().window().maximize();
	driver.manage().deleteAllCookies();
	driver.manage().deleteCookieNamed("sessionKey");
	driver.get("URL");

	//download commons-io.bin from apache and import to the project
	File src = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
	FileUtils.copyFile(src,new File("path"));


//# Handling Properties ============================================//
datadriven.properties // prop file
username="username" // define prop

Properties prop=new Properties();
FileInputStream fis=new FileInputStream(".prop path");
prop.load(fis);
prop.getProperty("property");
//=================================================================//



//# Working With nodes ==============================================//
	// Download selenium-server-standalone
	~$ java -jar selenium-server-standalone-3.8.2.jar -role hub // hub machine

	// Download selenium-server-standalone and chromedriver
	~$ java -Dwebdriver.chrome.driver=chromedriver.exe -jar selenium-server-standalone-3.8.2.jar 
	 -role webdriver -hub htt../grid/register -port 5566 // node machine

	DesiredCapabilities dc = new DesiredCapabilities();
	dc.setBrowserName("chrome");
	dc.setPlatform(Platform.WINDOWS);
	String localhost = "http://localhost:4444/wd/hub";
	WebDriver driver1 = new RemoteWebDriver(new URL(localhost),dc);
//=================================================================//



//# Working with Dates =============================================//
Date date = new Date();
SimpleDateFormat sdf = new SimpleDateFormat("d/mm/yyyy");
sdf.format(date);
//=================================================================//


//# POI ===========================================================//
// import
// https://mvnrepository.com/artifact/org.apache.poi/poi
// https://mvnrepository.com/artifact/org.apache.poi/poi-ooxml

FileInputStream fis = new FileInputStream("xlsx path");
XSSFWorkbook workbook = new XSSFWorkbook(fis));
workbook.getNumberOfSheets());
workbook.getSheetName(i));

XSSFSheet sheet = workbook.getSheetAt(i));
Iterator<Row> rows = sheet.iterator());
Row row = rows.next());

Iterator<Cell> cells = row.cellIterator());
cells.hasNext()); // T-F
Cell cell = cells.next());
//or  = row.getCell(coloumn));

 if (cell.getCellTypeEnum==CellType.String) {
	String value = cell.getStringValue();
 }else if (cell.getCellTypeEnum==CellType.Number){
 	String value = NumberToTextConverter.toText(
 		cell.getNumericCellValue());
 }
//=================================================================//


// OOP//===========================================================//
@FindBy(id="")
WebElement pass;
PageFactory.initElements(driver,this); // at the end of constructor
By passID= By.id("");
driver.findElement(passID);
//=================================================================//


//# Cucumber ======================================================//
@RunWith(Cucumber.class)
@CucumberOptions(
	features = "src/test/java/features", // or /features/file.feature for specification
	glue = "stepDefinitions")
//=================================================================//


// HashSet (Set) Doesn't store duplicates
// HashMap (Map) Key,value pair 

ArrayList<String> a = new ArrayList<String>;
a.add("");
a.add(i,"");
a.remove(""); //or i
a.get(i);
a.contains(""); // T-F
a.indexOf("");
a.isEmpty(); // T-F
a.size();

HashMap<Integer,String> hm = new HashMap<Integer,String>();
hm.put(i,"");
hm.remove(i);

Set s = hm.entrySet();



driver.navigate().forward(); // or back or refresh
driver.navigate().to(“url”);
driver.close(): To close current WebDriver instance
driver.quit(): To close all the opened WebDriver instances
 


@Test (dataProvider="getData")
public void loginTest(String Uid, String Pwd){
	System.out.println("UserName is "+ Uid);
	System.out.println("Password is "+ Pwd);
}
@DataProvider(name="getData")
public Object[][] getData(){
	Object [][] data = new Object [2][2];

	data [0][0] = "FirstUid";
	data [0][1] = "FirstPWD";

	data[1][0] = "SecondUid";
	data[1][1] = "SecondPWD";

	return data;
}