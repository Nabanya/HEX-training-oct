use("supply_chain");

db.shipment_logs.drop();

db.shipment_logs.insertMany([
  {
    shipment_id: "SH1001",
    order_id: "O0001",
    supplier_id: "S001",
    carrier: "BlueDart",
    status: "DELIVERED",
    events: [
      { ts: new Date("2026-01-06T09:00:00Z"), location: "Chennai",   note: "Picked up" },
      { ts: new Date("2026-01-10T14:30:00Z"), location: "Madurai",   note: "In transit" },
      { ts: new Date("2026-01-14T11:00:00Z"), location: "Sivakasi",  note: "Delivered" }
    ]
  },
  {
    shipment_id: "SH1002",
    order_id: "O0002",
    supplier_id: "S002",
    carrier: "DTDC",
    status: "DELIVERED",
    events: [
      { ts: new Date("2026-01-09T10:15:00Z"), location: "Bengaluru", note: "Picked up" },
      { ts: new Date("2026-01-17T16:45:00Z"), location: "Sivakasi",  note: "Delivered" }
    ]
  },
  {
    shipment_id: "SH1003",
    order_id: "O0003",
    supplier_id: "S003",
    carrier: "Delhivery",
    status: "IN_TRANSIT",
    events: [
      { ts: new Date("2026-01-11T08:00:00Z"), location: "Coimbatore", note: "Picked up" }
    ]
  }
]);

db.shipment_logs.createIndex({ shipment_id: 1 }, { unique: true });
db.shipment_logs.createIndex({ order_id: 1 });
db.shipment_logs.createIndex({ supplier_id: 1, status: 1 });   // compound
db.shipment_logs.createIndex({ "events.ts": -1 });             // latest events first

print("All in-transit shipments:");
printjson(db.shipment_logs.find({ status: "IN_TRANSIT" }).toArray());

print("Shipments per supplier:");
printjson(db.shipment_logs.aggregate([
  { $group: { _id: "$supplier_id", shipments: { $sum: 1 } } }
]).toArray());

print("Indexes:");
printjson(db.shipment_logs.getIndexes());

db.shipment_logs.updateOne(
  { shipment_id: "SH1003" },
  { $push: { events: { ts: new Date(), location: "Madurai", note: "In transit" } } }
);
