use supply_chain_db;
db.shipment_logs.drop();

db.shipment_logs.insertMany([
  { shipment_id: "SHP-1001", order_id: 1, supplier_id: 1, carrier: "DHL", status: "In Transit", location: "Hub Alpha", temperature_c: 4.2, created_at: ISODate("2026-10-02T08:00:00Z") },
  { shipment_id: "SHP-1002", order_id: 2, supplier_id: 2, carrier: "FedEx", status: "Delivered", location: "Facility Main", temperature_c: 21.0, created_at: ISODate("2026-10-04T12:30:00Z") },
  { shipment_id: "SHP-1003", order_id: 3, supplier_id: 3, carrier: "UPS", status: "Delayed", location: "Border Checkpoint", temperature_c: 18.5, created_at: ISODate("2026-10-05T09:15:00Z") },
  { shipment_id: "SHP-1004", order_id: 4, supplier_id: 4, carrier: "DHL", status: "Delivered", location: "Facility Main", temperature_c: 20.1, created_at: ISODate("2026-10-06T14:00:00Z") },
  { shipment_id: "SHP-1005", order_id: 5, supplier_id: 5, carrier: "FedEx", status: "Delayed", location: "Customs Clear", temperature_c: 5.0, created_at: ISODate("2026-10-08T11:45:00Z") },
  { shipment_id: "SHP-1006", order_id: 6, supplier_id: 6, carrier: "UPS", status: "Delivered", location: "Facility Main", temperature_c: 22.3, created_at: ISODate("2026-10-07T16:20:00Z") },
  { shipment_id: "SHP-1007", order_id: 7, supplier_id: 7, carrier: "DHL", status: "Exception", location: "Hub Beta", temperature_c: -2.0, created_at: ISODate("2026-10-08T10:00:00Z") },
  { shipment_id: "SHP-1008", order_id: 8, supplier_id: 8, carrier: "FedEx", status: "In Transit", location: "Highway Station", temperature_c: 19.0, created_at: ISODate("2026-10-09T07:10:00Z") },
  { shipment_id: "SHP-1009", order_id: 9, supplier_id: 9, carrier: "UPS", status: "Delivered", location: "Facility Main", temperature_c: 21.5, created_at: ISODate("2026-10-09T18:00:00Z") },
  { shipment_id: "SHP-1010", order_id: 10, supplier_id: 10, carrier: "DHL", status: "Delayed", location: "Port West", temperature_c: 25.0, created_at: ISODate("2026-10-11T13:40:00Z") },
  { shipment_id: "SHP-1011", order_id: 11, supplier_id: 11, carrier: "FedEx", status: "Delivered", location: "Facility Main", temperature_c: 20.0, created_at: ISODate("2026-10-10T15:00:00Z") },
  { shipment_id: "SHP-1012", order_id: 12, supplier_id: 12, carrier: "UPS", status: "In Transit", location: "Hub Gamma", temperature_c: 17.8, created_at: ISODate("2026-10-10T19:30:00Z") },
  { shipment_id: "SHP-1013", order_id: 13, supplier_id: 13, carrier: "DHL", status: "Delayed", location: "Customs Clear", temperature_c: 3.8, created_at: ISODate("2026-10-12T10:15:00Z") },
  { shipment_id: "SHP-1014", order_id: 14, supplier_id: 14, carrier: "FedEx", status: "Delivered", location: "Facility Main", temperature_c: 21.1, created_at: ISODate("2026-10-11T11:00:00Z") },
  { shipment_id: "SHP-1015", order_id: 15, supplier_id: 15, carrier: "UPS", status: "Delayed", location: "Hub Delta", temperature_c: 19.4, created_at: ISODate("2026-10-14T08:50:00Z") }
]);

db.shipment_logs.createIndex({ supplier_id: 1 });
db.shipment_logs.createIndex({ status: 1 });