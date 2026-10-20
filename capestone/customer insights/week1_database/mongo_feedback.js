use customer_orders_db;
db.customer_feedback.drop();

db.customer_feedback.insertMany([
  { feedback_id: 101, customer_id: 1, order_id: 1, rating: 2, issue_category: "Late Delivery", comments: "Arrived 3 days late.", created_at: ISODate("2026-10-09T10:00:00Z") },
  { feedback_id: 102, customer_id: 2, order_id: 2, rating: 5, issue_category: "None", comments: "Perfect experience.", created_at: ISODate("2026-10-05T11:00:00Z") },
  { feedback_id: 103, customer_id: 3, order_id: 3, rating: 1, issue_category: "Damaged Goods", comments: "Late and box was broken.", created_at: ISODate("2026-10-11T12:00:00Z") },
  { feedback_id: 104, customer_id: 4, order_id: 4, rating: 4, issue_category: "None", comments: "Good service.", created_at: ISODate("2026-10-07T09:00:00Z") },
  { feedback_id: 105, customer_id: 5, order_id: 5, rating: 2, issue_category: "Weather Delay", comments: "Took way too long.", created_at: ISODate("2026-10-13T14:00:00Z") },
  { feedback_id: 106, customer_id: 1, order_id: 6, rating: 5, issue_category: "None", comments: "Fast shipment.", created_at: ISODate("2026-10-08T15:00:00Z") },
  { feedback_id: 107, customer_id: 6, order_id: 7, rating: 1, issue_category: "Driver Issue", comments: "Driver lost the address.", created_at: ISODate("2026-10-09T16:00:00Z") },
  { feedback_id: 108, customer_id: 7, order_id: 8, rating: 3, issue_category: "Traffic Delay", comments: "Slight delay.", created_at: ISODate("2026-10-10T10:00:00Z") },
  { feedback_id: 109, customer_id: 8, order_id: 9, rating: 5, issue_category: "None", comments: "Delivered as promised.", created_at: ISODate("2026-10-10T11:00:00Z") },
  { feedback_id: 110, customer_id: 9, order_id: 10, rating: 2, issue_category: "Late Delivery", comments: "Severe delay.", created_at: ISODate("2026-10-15T08:00:00Z") },
  { feedback_id: 111, customer_id: 10, order_id: 11, rating: 4, issue_category: "None", comments: "Satisfied.", created_at: ISODate("2026-10-11T13:00:00Z") },
  { feedback_id: 112, customer_id: 11, order_id: 12, rating: 1, issue_category: "Wrong Item", comments: "Still waiting and wrong item listed.", created_at: ISODate("2026-10-12T17:00:00Z") },
  { feedback_id: 113, customer_id: 12, order_id: 13, rating: 2, issue_category: "Traffic Delay", comments: "4 days delay.", created_at: ISODate("2026-10-16T18:00:00Z") },
  { feedback_id: 114, customer_id: 13, order_id: 14, rating: 5, issue_category: "None", comments: "Smooth delivery.", created_at: ISODate("2026-10-12T09:00:00Z") },
  { feedback_id: 115, customer_id: 14, order_id: 15, rating: 1, issue_category: "Damaged Goods", comments: "Very late and damaged.", created_at: ISODate("2026-10-19T10:00:00Z") }
]);

db.customer_feedback.createIndex({ customer_id: 1 });