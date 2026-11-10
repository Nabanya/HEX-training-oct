
use("customer_orders");

db.customer_feedback.drop();

db.customer_feedback.insertMany([
  {
    customer_id: 1,
    order_id: "ORD0001",
    rating: 2,
    comment: "Package arrived 3 days late and the box was dented.",
    tags: ["late", "damaged"],
    created_at: new Date("2026-03-10T10:00:00Z")
  },
  {
    customer_id: 1,
    order_id: "ORD0002",
    rating: 5,
    comment: "Fast delivery, thank you!",
    created_at: new Date("2026-03-15T09:30:00Z")
  },
  {
    customer_id: 2,
    order_id: "ORD0003",
    rating: 3,
    comment: "Delayed because of rain, but the courier kept me updated.",
    tags: ["late", "weather"],
    courier_rating: 4,
    created_at: new Date("2026-03-23T18:20:00Z")
  },
  {
    customer_id: 3,
    order_id: "ORD0004",
    rating: 4,
    comment: "Good service.",
    created_at: new Date("2026-03-20T12:00:00Z")
  }
]);

db.customer_feedback.createIndex({ customer_id: 1 });

print("Feedback for customer 1:");
printjson(db.customer_feedback.find({ customer_id: 1 }).toArray());

print("Query plan (should show IXSCAN, i.e. the index is used):");
printjson(
  db.customer_feedback.find({ customer_id: 1 }).explain("queryPlanner")
    .queryPlanner.winningPlan
);

print("Average rating per customer:");
printjson(db.customer_feedback.aggregate([
  { $group: { _id: "$customer_id", avg_rating: { $avg: "$rating" } } }
]).toArray());

print("Indexes:");
printjson(db.customer_feedback.getIndexes());
