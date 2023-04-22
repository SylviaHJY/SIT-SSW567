//*******************************************************************
//  __description__ = "Assignment 01 - Unit Testing"
//  __course__ = "ics615"
//  __organization__ = "Information and Computer Sciences Department, University of Hawai‘i at Mānoa"
//  __author__ = "Anthony Peruma"
//  __email__ = "peruma@hawaii.edu"
//  __web__ = "https://www.peruma.me"
//  __version__ = "1.0"
//  __created__ = "2022-08-01"
//  __modified__ = "2023-03-01"
//  __maintainer__ = "Anthony Peruma"
//*******************************************************************
package edu.hawaii.ics.peruma;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class VendingMachineTest {

    private static final double PRICE_SODA = 1.25;
    private static final double PRICE_CHIPS = 1.50;
    private static final double PRICE_APPLE_JUICE = 2.25;
    private static final double DELTA = 0.001;

    VendingMachine vendingMachine;

    @Before
    public void setUp(){
        vendingMachine = new VendingMachine();
        vendingMachine.addItem(new Item("Soda", PRICE_SODA, 10, new Location(1, 1)));
        vendingMachine.addItem(new Item("Chips", PRICE_CHIPS, 5, new Location(1, 2)));
    }

    @Test
    public void testAddItem_Successful() {
        assertAddItem(new Item("Apple Juice", PRICE_APPLE_JUICE, 10, new Location(3, 1)), AddStatus.AddMessage.SUCCESS);
    }

    @Test
    public void testInitialization() {
        assertNotNull(vendingMachine.getItems());
        assertEquals(2, vendingMachine.getItems().size());
    }

    @Test
    public void testAddItem_InvalidLocation() {
        assertAddItem(new Item("Apple Juice", PRICE_APPLE_JUICE, 10, new Location(11, 1)), AddStatus.AddMessage.INVALID_LOCATION);
    }

    @Test
    public void testAddItem_InsufficientSpace() {
        assertAddItem(new Item("Apple Juice", PRICE_APPLE_JUICE, 11, new Location(3, 1)), AddStatus.AddMessage.INSUFFICIENT_SPACE);
    }

    @Test
    public void testVendItem_InsufficientFunds() {
        assertVendItem(new Location(1, 1), 1.00, VendingStatus.VendingMessage.INSUFFICIENT_FUNDS, null);
    }

    @Test
    public void testVendItem_UnknownLocation() {
        assertVendItem(new Location(5, 5), PRICE_SODA, VendingStatus.VendingMessage.UNKNOWN_LOCATION, null);
    }

    @Test
    public void testLocationEquals() {
        Location location1 = new Location(1, 1);
        Location location2 = new Location(1, 1);
        Location location3 = new Location(1, 2);
        assertTrue(location1.equals(location2));
        assertFalse(location1.equals(location3));
    }

    @Test
    public void testVendItem_OutOfStock() {
        VendingStatus vendingStatus;
        for (int i = 0; i < 10; i++) {
            vendingStatus = vendingMachine.vendItem(new Location(1, 1), PRICE_SODA);
        }
        assertVendItem(new Location(1, 1), PRICE_SODA, VendingStatus.VendingMessage.OUT_OF_STOCK, null);
    }

    private void assertAddItem(Item item, AddStatus.AddMessage expectedMessage) {
        AddStatus addStatus = vendingMachine.addItem(item);
        assertEquals(expectedMessage, addStatus.getAddMessage());
    }

    private void assertVendItem(Location location, double payment, VendingStatus.VendingMessage expectedMessage, Double expectedChange) {
        VendingStatus vendingStatus = vendingMachine.vendItem(location, payment);
        assertEquals(expectedMessage, vendingStatus.getMessage());
        if (expectedChange != null) {
            assertEquals(expectedChange, vendingStatus.getChange(), DELTA);
        }
    }
}

